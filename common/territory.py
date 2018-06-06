from .settlements import get_settlement_details
from .utils import get_effects_summary


def get_hex_details(hex):
    # attributes
    features = []
    hex.has_river = False
    hex.has_coast = False
    hex.has_settlement = False
    hex.has_capital = False
    # settlements
    for settlement in hex.settlement.all():
        features.append(settlement.name)
        if settlement.capital:
            hex.has_capital = True
        else:
            hex.has_settlement = True
    # features
    for feature in hex.features.all():
        features.append(feature.name)
        if feature.name.lower() == "coastline":
            hex.has_coast = True
        if feature.name.lower() == "river":
            hex.has_river = True
    # improvements
    for improvement in hex.improvements.all():
        features.append(improvement.name)
    # hex summary
    hex.features_summary = ', '.join(features)
    # image
    ### plains
    if hex.type.id == 1:
        if hex.has_coast and hex.has_river and hex.has_settlement:
            hex.img = 'img/terrain/plains/plains-river-coast-settlement.png'
        elif hex.has_coast and hex.has_river:
            hex.img = 'img/terrain/plains/plains-river-coast.png'
        elif hex.has_coast:
            hex.img = 'img/terrain/plains/plains-coast.png'
        elif hex.has_river:
            hex.img = 'img/terrain/plains/plains-river.png'
        else:
            hex.img = 'img/terrain/plains/plains.png'
    ### desert
    elif hex.type.id == 4:
        if hex.has_coast and hex.has_river and hex.has_settlement:
            hex.img = 'img/terrain/hills/hills-river-coast-settlement.png'
        elif hex.has_coast and hex.has_river:
            hex.img = 'img/terrain/hills/hills-river-coast.png'
        elif hex.has_coast:
            hex.img = 'img/terrain/hills/hills-coast.png'
        elif hex.has_river:
            hex.img = 'img/terrain/hills/hills-river.png'
        else:
            hex.img = 'img/terrain/hills/hills.png'
    ### forest
    elif hex.type.id == 5:
        if hex.has_coast and hex.has_river and hex.has_settlement:
            hex.img = 'img/terrain/forest/forest-river-coast-settlement.png'
        elif hex.has_coast and hex.has_river:
            hex.img = 'img/terrain/forest/forest-river-coast.png'
        elif hex.has_coast:
            hex.img = 'img/terrain/forest/forest-coast.png'
        elif hex.has_river:
            hex.img = 'img/terrain/forest/forest-river.png'
        else:
            hex.img = 'img/terrain/forest/forest.png'
    ### hills
    elif hex.type.id == 6:
        if hex.has_coast and hex.has_river and hex.has_capital:
            hex.img = 'img/terrain/hills/hills-river-coast-capital.png'
        elif hex.has_coast and hex.has_river and hex.has_settlement:
            hex.img = 'img/terrain/hills/hills-river-coast-settlement.png'
        elif hex.has_coast and hex.has_river:
            hex.img = 'img/terrain/hills/hills-river-coast.png'
        elif hex.has_coast:
            hex.img = 'img/terrain/hills/hills-coast.png'
        elif hex.has_river:
            hex.img = 'img/terrain/hills/hills-river.png'
        else:
            hex.img = 'img/terrain/hills/hills.png'
    ### marsh
    elif hex.type.id == 7:
        if hex.has_coast and hex.has_river and hex.has_settlement:
            hex.img = 'img/terrain/marsh/marsh-river-coast-settlement.png'
        elif hex.has_coast and hex.has_river:
            hex.img = 'img/terrain/marsh/marsh-river-coast.png'
        elif hex.has_coast:
            hex.img = 'img/terrain/marsh/marsh-coast.png'
        elif hex.has_river:
            hex.img = 'img/terrain/marsh/marsh-river.png'
        else:
            hex.img = 'img/terrain/marsh/marsh.png'
    ### jungle
    elif hex.type.id == 8:
        if hex.has_coast and hex.has_river and hex.has_settlement:
            hex.img = 'img/terrain/jungle/jungle-river-coast-settlement.png'
        elif hex.has_coast and hex.has_river:
            hex.img = 'img/terrain/jungle/jungle-river-coast.png'
        elif hex.has_coast:
            hex.img = 'img/terrain/jungle/jungle-coast.png'
        elif hex.has_river:
            hex.img = 'img/terrain/jungle/jungle-river.png'
        else:
            hex.img = 'img/terrain/jungle/jungle.png'
    ### mountains
    elif hex.type.id == 9:
        if hex.has_coast and hex.has_river and hex.has_settlement:
            hex.img = 'img/terrain/mountains/mountains-river-coast-settlement.png'
        elif hex.has_coast and hex.has_river:
            hex.img = 'img/terrain/mountains/mountains-river-coast.png'
        elif hex.has_coast:
            hex.img = 'img/terrain/mountains/mountains-coast.png'
        elif hex.has_river:
            hex.img = 'img/terrain/mountains/mountains-river.png'
        else:
            hex.img = 'img/terrain/mountains/mountains.png'
    ### water
    elif hex.type.id == 10:
        hex.img = 'img/terrain/water/water.png'
    # filter
    hex.filter = 'sepia(60%)'
    if hex.polity is not None and hex.map is not None:
        if hex.polity.id == 1:
            hex.filter = 'none'
    return {}


def get_territory_effects(territories):
    for territory in territories:
        # set base by type of terrain
        territory.pop_bonus = territory.type.pop_bonus
        territory.dan_bonus = territory.type.dan_bonus
        territory.eco_bonus = 0
        territory.loy_bonus = 0
        territory.sta_bonus = 0
        territory.fam_bonus = 0
        territory.inf_bonus = 0
        territory.cor_bonus = 0
        territory.cri_bonus = 0
        territory.law_bonus = 0
        territory.lor_bonus = 0
        territory.pro_bonus = 0
        territory.soc_bonus = 0
        territory.def_bonus = 0
        territory.con_bonus = 0
        territory.con_bonus_from_farms = 0
        territory.inc_bonus = 0
        territory.unr_bonus = 0

        # special vars
        has_lair = False
        has_watchtower = False
        has_fort = False
        has_landmark = False
        has_road = False
        has_highway = False
        has_resource = False
        has_farm = False
        has_fishery = False
        has_automatons = False
        has_deathless = False
        has_mine = False
        improvements = []
        # mine types
        tier_1 = ['iron', 'salt', 'coal', 'copper']
        tier_2 = ['gold', 'silver', 'gems']
        tier_3 = ['adamantium', 'platinum', 'mithril']
        tier_1_resource = False
        tier_2_resource = False
        tier_3_resource = False

        # add bonuses from each improvement
        for improvement in territory.improvements.all():
            territory.pop_bonus += improvement.pop_bonus
            territory.dan_bonus += improvement.dan_bonus
            territory.eco_bonus += improvement.eco_bonus
            territory.loy_bonus += improvement.loy_bonus
            territory.sta_bonus += improvement.sta_bonus
            territory.fam_bonus += improvement.fam_bonus
            territory.inf_bonus += improvement.inf_bonus
            territory.def_bonus += improvement.def_bonus
            territory.con_bonus += improvement.con_bonus
            territory.inc_bonus += improvement.inc_bonus
            territory.unr_bonus += improvement.unr_bonus
            # farms
            if improvement.name.lower() == 'farm':
                territory.con_bonus_from_farms += abs(improvement.con_bonus)
            # rules flags
            if improvement.name.lower() == 'watchtower': has_watchtower = True
            if improvement.name.lower() == 'fort': has_fort = True
            if improvement.name.lower() == 'road': has_road = True
            if improvement.name.lower() == 'highway': has_highway = True
            if improvement.name.lower() == 'farm': has_farm = True
            if improvement.name.lower() == 'fishery': has_fishery = True
            if improvement.name.lower() in ['mine', 'quarry', 'sawmill']:
                improvements.append(improvement)
            if improvement.name.lower() == 'animated automation': has_automatons = True
            if improvement.name.lower() == 'deathless laborers': has_deathless = True
            if improvement.name.lower() == 'mine': has_mine = True

        # add bonuses from each feature
        for feature in territory.features.all():
            territory.pop_bonus += feature.pop_bonus
            territory.dan_bonus += feature.dan_bonus
            territory.eco_bonus += feature.eco_bonus
            territory.loy_bonus += feature.loy_bonus
            territory.sta_bonus += feature.sta_bonus
            territory.def_bonus += feature.def_bonus
            territory.con_bonus += feature.con_bonus
            territory.inc_bonus += feature.inc_bonus
            territory.unr_bonus += feature.unr_bonus
            # rules flags
            if feature.name.lower() == 'lair': has_lair = True
            if feature.name.lower() == 'landmark': has_landmark = True
            if 'resource' in feature.name.lower():
                has_resource = True
                for t in tier_1:
                    if t in feature.name.lower():
                        tier_1_resource = True
                for t in tier_2:
                    if t in feature.name.lower():
                        tier_2_resource = True
                for t in tier_3:
                    if t in feature.name.lower():
                        tier_3_resource = True

        # add bonuses from settlement
        for settlement in territory.settlement.all():
            get_settlement_details(settlement)
            territory.dan_bonus += settlement.danger
            territory.the_settlement = settlement
            for festival in settlement.festival.all():
                if festival.type.name.lower() == 'civic': territory.civic_festival = True
                if festival.type.name.lower() == 'religious': territory.religious_festival = True

        # add rules bonuses
        if has_lair and (has_fort or has_watchtower): territory.def_bonus += 1
        if has_landmark and (has_road or has_highway): territory.loy_bonus += 1
        if len(improvements) > 0:
            for improvement in improvements:
                if improvement.eco_bonus != 0: territory.eco_bonus += 1
                if improvement.loy_bonus != 0: territory.loy_bonus += 1
                if improvement.sta_bonus != 0: territory.sta_bonus += 1
                if improvement.def_bonus != 0: territory.def_bonus += 1
                if improvement.inc_bonus != 0: territory.inc_bonus += 1
                if has_automatons or has_deathless: territory.inc_bonus += 1
        if has_resource and (has_farm or has_fishery): territory.con_bonus -= 1
        if (has_automatons or has_deathless) and (has_farm or has_fishery):
            territory.con_bonus -= 1
        if has_mine:
            if tier_1_resource: territory.inc_bonus += 1
            elif tier_2_resource: territory.inc_bonus += 2
            elif tier_3_resource: territory.inc_bonus += 3

        # festival modifiers
        territory.civic_festival = False
        territory.religious_festival = False
        for festival in territory.festival.all():
            if festival.type.name.lower() == 'civic': territory.civic_festival = True
            if festival.type.name.lower() == 'religious': territory.religious_festival = True

        # build effects summary
        territory.effects_summary = get_effects_summary(territory)
        if territory.civic_festival or territory.religious_festival:
            territory.effects_summary += ', FESTIVAL IN PROGRESS (stability checks here -2)'

    return {'territories': territories}
