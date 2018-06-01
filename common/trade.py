import math
from .polity import get_polity_details
from .utils import get_signed_number
from .settlements import get_settlement_details


def get_trade_route_details(trade_route, polity):
    # attributes
    trade_route.eco_bonus = 0
    trade_route.fam_bonus = 0
    # get desc
    trade_route.desc = trade_route.get_description()
    # determine route modifier
    trade_route.route_modifier = math.floor(trade_route.length / 10)
    # determine length modifier
    trade_route.length_modifier = polity.size.total - trade_route.length
    if trade_route.length_modifier < 0: trade_route.length_modifier = 0
    # get route DC
    trade_route.dc = polity.control_dc + polity.corruption.total + trade_route.route_modifier + \
        trade_route.length_modifier - polity.productivity.total
    # determine return on investment
    trade_route.roi = ''
    if trade_route.success_level is not None:
        trade_route.eco_bonus += trade_route.success_level.eco_bonus
        trade_route.fam_bonus += trade_route.success_level.fam_bonus
        if trade_route.success_level.name.lower() == 'failure':
            trade_route.roi = '+%sd4 BP' % trade_route.investment
        elif trade_route.success_level.name.lower() in ['success', 'great success']:
            trade_route.roi = '%s+%sd4 BP' % (trade_route.route_modifier, (trade_route.investment * 2))

    # get food route bonuses
    settlement = None
    if trade_route.success_level is not None \
            and trade_route.type.name.lower() == 'food'\
            and polity.consumption_excess:
        has_granary = False
        has_stockyard = False
        if settlement is None:
            settlement = get_settlement_details(trade_route.settlement)['settlement']
        for building in settlement.buildings:
            if building.type.name.lower() == 'granary': has_granary = True
            if building.type.name.lower() == 'stockyard': has_stockyard = True
            if has_granary and has_stockyard: break
        if has_granary and has_stockyard:
            food_sources = 0
            for territory in polity.territory.all():
                for improvement in territory.improvements.all():
                    if improvement.name.lower() in ['farm', 'fishery', 'winery']:
                        food_sources += 1
            trade_route.eco_bonus += math.floor(food_sources / 10)
    # get goods route bonuses
    if trade_route.success_level is not None and trade_route.type.name.lower() == 'goods':
        has_guildhall = False
        goods_sources = 0
        if settlement is None:
            settlement = get_settlement_details(trade_route.settlement)['settlement']
        for building in settlement.buildings:
            if building.type.name.lower() == 'guildhall':
                has_guildhall = True
                goods_sources += 1
            if building.type.name.lower() in [
                'smithy', 'shop', 'trade shop', 'fletcher', 'carpenter', 'weaver', 'tannery'
            ]:
                goods_sources += 1
        if has_guildhall:
            trade_route.eco_bonus += math.floor(goods_sources / 10)
    # get luxury route bonuses
    if trade_route.success_level is not None and trade_route.type.name.lower() == 'luxuries':
        has_luxury_store = False
        sources = 0
        if settlement is None:
            settlement = get_settlement_details(trade_route.settlement)['settlement']
        for building in settlement.buildings:
            if building.type.name.lower() == 'luxury store':
                has_luxury_store = True
                sources += 1
            if building.type.name.lower() in [
                'alchemist', "caster's tower", 'exotic artisan', 'herbalist', 'magic shop'
            ]:
                sources += 1
        if has_luxury_store:
            trade_route.eco_bonus += math.floor(sources / 10)
    # get raw materials route bonuses
    if trade_route.success_level is not None \
            and trade_route.type.name.lower() == 'raw materials':
        has_foundry = False
        sources = 0
        if settlement is None:
            settlement = get_settlement_details(trade_route.settlement)['settlement']
        for building in settlement.buildings:
            if building.type.name.lower() == 'foundry': has_foundry = True
        if has_foundry:
            for territory in polity.territory.all():
                for improvement in territory.improvements.all():
                    if improvement.name.lower() in ['mine', 'quarry', 'camp', 'sawmill']:
                        sources += 1
            trade_route.eco_bonus += math.floor(sources / 10)

    # get outcome summary
    effects = []
    if trade_route.success_level is not None:
        if trade_route.success_level.fam_bonus != 0:
            effects.append('%s fame' % get_signed_number(trade_route.fam_bonus)['s'])
        if trade_route.success_level.eco_bonus != 0:
            effects.append('%s economy' % get_signed_number(trade_route.eco_bonus)['s'])
        if trade_route.success_level.fame_increment != 0:
            effects.append(
                '%s fame (permanent)' % get_signed_number(
                    trade_route.success_level.unrest_increment
                )['s']
            )
        if trade_route.success_level.unrest_increment != 0:
            effects.append(
                '%s unrest (permanent)' % get_signed_number(
                    trade_route.success_level.unrest_increment
                )['s']
            )
    if trade_route.roi != '':
        effects.append(trade_route.roi)
    trade_route.outcome_summary = ', '.join(effects)
    return {'trade route': trade_route}
