from .settlements import get_settlement_details
from .utils import get_effects_summary


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
        improvements = []

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
            if feature.name.lower() == 'resource': has_resource = True

        # add bonuses from settlement
        for settlement in territory.settlement.all():
            get_settlement_details(settlement)
            territory.dan_bonus += settlement.danger
            territory.the_settlement = settlement

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

        # build effects summary
        territory.effects_summary = get_effects_summary(territory)

    return {'territories': territories}
