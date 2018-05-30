import math
from settlements.models import Type
from .utils import get_effects_summary_for_obj


def get_settlement_details(settlement):
    # define attributes
    settlement.buildings = settlement.building.all()
    settlement.lots = 0
    settlement.att_summary = ''
    # major
    settlement.economy = 0
    settlement.loyalty = 0
    settlement.stability = 0
    # minor
    settlement.fame = 0
    settlement.infamy = 0
    settlement.corruption = 0
    settlement.crime = 0
    settlement.law = 0
    settlement.lore = 0
    settlement.productivity = 0
    settlement.society = 0
    # other
    settlement.population = 0
    settlement.danger = 0
    settlement.income = 0
    settlement.defense = 0
    settlement.unrest = 0
    settlement.consumption = 0
    settlement.magic_items = []
    settlement.magic_items_string = ''
    settlement.endowment_upkeep = 0

    # apply building modifiers
    for building in settlement.buildings:
        get_building_details(building)
        # lots
        settlement.lots += building.lots
        # attributes
        settlement.population += building.population
        settlement.danger += building.danger
        settlement.economy += building.economy
        settlement.loyalty += building.loyalty
        settlement.stability += building.stability
        settlement.fame += building.fame
        settlement.infamy += building.infamy
        settlement.corruption += building.corruption
        settlement.crime += building.crime
        settlement.law += building.law
        settlement.lore += building.lore
        settlement.productivity += building.productivity
        settlement.society += building.society
        settlement.defense += building.defense
        settlement.consumption += building.consumption
        settlement.income += building.income
        settlement.unrest += building.unrest
        if building.type.magic_items != '':
            settlement.magic_items.append(building.type.magic_items)
        settlement.endowment_upkeep += building.endowment_upkeep

    # determine type
    if settlement.districts > 0:
        settlement.type = Type.objects.get(name="Metropolis")
    elif settlement.lots > 16:
        settlement.type = Type.objects.get(name="City")
    elif settlement.lots > 4:
        settlement.type = Type.objects.get(name="Town")
    else:
        settlement.type = Type.objects.get(name="Village")

    # apply type modifiers
    if settlement.type != Type.objects.get(name="Metropolis"):
        settlement.consumption = math.floor(settlement.consumption + settlement.type.con_bonus)
    else:
        settlement.consumption = math.floor(
            settlement.consumption + (settlement.type.con_bonus * settlement.districts))
    settlement.population = math.floor(settlement.population * settlement.type.pop_mult)
    settlement.danger += settlement.type.dan_mod
    settlement.magic_items.insert(0, settlement.type.magic_items)

    # summary
    settlement.att_summary = get_effects_summary_for_obj(settlement)
    settlement.magic_items_string = ', '.join(settlement.magic_items)
    if settlement.endowment_upkeep > 0:
        settlement.att_summary += ', %sgp endowment upkeep' % settlement.endowment_upkeep

    return {'settlement': settlement}


def get_building_details(building):
    # building attributes
    building.population = 0
    building.danger = 0
    # major
    building.economy = 0
    building.loyalty = 0
    building.stability = 0
    # minor
    building.fame = 0
    building.infamy = 0
    building.corruption = 0
    building.crime = 0
    building.law = 0
    building.lore = 0
    building.productivity = 0
    building.society = 0
    # other
    building.defense = 0
    building.consumption = 0
    building.endowment_upkeep = 0
    building.unrest = 0
    building.income = 0

    # apply type modifiers
    if building.lots is None:
        building.lots = building.type.lots
    else:
        building.lots = building.lots
    building.population += building.type.pop_bonus
    building.danger += building.type.dan_bonus
    building.economy += building.type.eco_bonus
    building.loyalty += building.type.loy_bonus
    building.stability += building.type.sta_bonus
    building.fame += building.type.fam_bonus
    building.infamy += building.type.inf_bonus
    building.corruption += building.type.cor_bonus
    building.crime += building.type.cri_bonus
    building.law += building.type.law_bonus
    building.lore += building.type.lor_bonus
    building.productivity += building.type.pro_bonus
    building.society += building.type.soc_bonus
    building.defense += building.type.def_bonus
    building.consumption += building.type.con_bonus
    building.income += building.type.inc_bonus
    building.unrest += building.type.unr_bonus

    # apply enhancement modifiers
    building.enhancements_list = []
    for enhancement in building.enhancements.all():
        building.enhancements_list.append(enhancement.name)
        building.population += enhancement.pop_bonus
        building.danger += enhancement.dan_bonus
        building.economy += enhancement.eco_bonus
        building.loyalty += enhancement.loy_bonus
        building.stability += enhancement.sta_bonus
        building.fame += enhancement.fam_bonus
        building.infamy += enhancement.inf_bonus
        building.corruption += enhancement.cor_bonus
        building.crime += enhancement.cri_bonus
        building.law += enhancement.law_bonus
        building.lore += enhancement.lor_bonus
        building.productivity += enhancement.pro_bonus
        building.society += enhancement.soc_bonus
        building.defense += enhancement.def_bonus
        building.consumption += enhancement.con_bonus
        building.income += enhancement.inc_bonus
        building.unrest += enhancement.unr_bonus

    # endowment
    if building.endowment:
        building.fame += 1
        building.loyalty += 1
        if not building.free_endowment:
            building.consumption += 1
            building.endowment_upkeep += (building.type.const_cost * building.type.const_time) * 100

    # effects summary
    building.effects_summary = get_effects_summary_for_obj(building)
    if building.endowment_upkeep > 0:
        building.effects_summary += ', %sgp endowment upkeep' % building.endowment_upkeep
    return {}
