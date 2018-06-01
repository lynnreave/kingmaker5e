import math
from .polity import get_polity_details
from .utils import get_signed_number


def get_trade_route_details(trade_route):
    # get desc
    trade_route.desc = trade_route.get_description()
    # determine route modifier
    trade_route.route_modifier = math.floor(trade_route.length / 10)
    # determine length modifier
    polity = get_polity_details(trade_route.polity.id)['polity']
    trade_route.length_modifier = polity.size.total - trade_route.length
    if trade_route.length_modifier < 0: trade_route.length_modifier = 0
    # get route DC
    trade_route.dc = polity.control_dc + polity.corruption.total + trade_route.route_modifier + \
        trade_route.length_modifier - polity.productivity.total
    # determine return on investment
    trade_route.roi = ''
    if trade_route.success_level is not None:
        if trade_route.success_level.name.lower() == 'failure':
            trade_route.roi = '+%sd4 BP' % trade_route.investment
        elif trade_route.success_level.name.lower() in ['success', 'great success']:
            trade_route.roi = '%s+%sd4 BP' % (trade_route.route_modifier, (trade_route.investment * 2))
    # get outcome summary
    effects = []
    if trade_route.success_level is not None:
        if trade_route.success_level.fam_bonus != 0:
            effects.append('%s fame' % get_signed_number(trade_route.success_level.fam_bonus)['s'])
        if trade_route.success_level.eco_bonus != 0:
            effects.append('%s economy' % get_signed_number(trade_route.success_level.eco_bonus)['s'])
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
