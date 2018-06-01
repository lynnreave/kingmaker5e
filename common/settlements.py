import math
from settlements.models import Type
from .utils import get_effects_summary_for_obj
from festivals.models import CIVIC_BUILDINGS, RELIGIOUS_BUILDINGS


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

    # if festival
    settlement.civic_festival = False
    settlement.religious_festival = False
    settlement.festival_effect_mult = 1.0
    for festival in settlement.festival.all():
        if festival.type.name.lower() == 'civic': settlement.civic_festival = True
        if festival.type.name.lower() == 'religious': settlement.religious_festival = True
        settlement.festival_effect_mult = festival.success_level.effect_mult

    # apply building modifiers
    for building in settlement.buildings:
        get_building_details(building)
        # lots
        settlement.lots += building.lots
        # festival effects
        # civil
        effect_mult = 1.0
        if settlement.civic_festival and building.type.name.lower() in CIVIC_BUILDINGS:
            effect_mult = settlement.festival_effect_mult
        # religious
        if settlement.religious_festival and building.type.name.lower() in RELIGIOUS_BUILDINGS:
            effect_mult = settlement.festival_effect_mult
        # attributes
        settlement.population += building.population
        settlement.danger += building.danger
        settlement.economy += math.floor(building.economy * effect_mult)
        settlement.loyalty += math.floor(building.loyalty * effect_mult)
        settlement.stability += math.floor(building.stability * effect_mult)
        settlement.fame += math.floor(building.fame * effect_mult)
        settlement.infamy += math.floor(building.infamy * effect_mult)
        settlement.corruption += math.floor(building.corruption * effect_mult)
        settlement.crime += math.floor(building.crime * effect_mult)
        settlement.law += math.floor(building.law * effect_mult)
        settlement.lore += math.floor(building.lore * effect_mult)
        settlement.productivity += math.floor(building.productivity * effect_mult)
        settlement.society += math.floor(building.society * effect_mult)
        settlement.defense += math.floor(building.defense * effect_mult)
        settlement.consumption += math.floor(building.consumption * effect_mult)
        settlement.income += math.floor(building.income * effect_mult)
        settlement.unrest += building.unrest
        if building.magic_items != '' and building.magic_items is not None:
            settlement.magic_items.append(building.magic_items)
            if settlement.civic_festival and building.type.name.lower() in CIVIC_BUILDINGS:
                settlement.magic_items.append(building.magic_items)
            if settlement.religious_festival and building.type.name.lower() in RELIGIOUS_BUILDINGS:
                settlement.magic_items.append(building.magic_items)
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
    if settlement.civic_festival or settlement.religious_festival:
        settlement.att_summary += ', FESTIVAL IN PROGRESS (stability checks here -2)'

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
    building.magic_items = building.type.magic_items

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

    # apply deity bonuses to religious buildings
    if building.deity is not None and building.type.name.lower() in ['shrine', 'temple', 'cathedral']:
        apply_deity_bonuses(building)


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


def apply_deity_bonuses(building):
    if building.deity.name == "Great Church":
        if building.type.name.lower() == 'cathedral':
            building.loyalty += 4
            building.stability += 4
            building.unrest -= 4
            building.law += 2
        elif building.type.name.lower() == 'temple':
            building.loyalty += 2
            building.stability += 2
            building.unrest -= 2
        elif building.type.name.lower() == 'shrine':
            building.loyalty += 1
            building.unrest -= 1
    elif building.deity.name == "Urian":
        if building.type.name.lower() == 'cathedral':
            building.loyalty += 4
            building.unrest -= 4
            building.defense += 2
            building.law += 2
        elif building.type.name.lower() == 'temple':
            building.defense += 2
            building.stability += 2
            building.unrest -= 2
        elif building.type.name.lower() == 'shrine':
            building.stability += 1
            building.unrest -= 1
    elif building.deity.name == "Shalimyr":
        if building.type.name.lower() == 'cathedral':
            building.economy += 4
            building.loyalty += 4
            building.stability += 4
            building.productivity += 3
        elif building.type.name.lower() == 'temple':
            building.economy += 3
            building.stability += 2
            building.productivity += 3
            building.crime += 1
        elif building.type.name.lower() == 'shrine':
            building.economy += 2
    elif building.deity.name == "Rontra":
        if building.type.name.lower() == 'cathedral':
            building.loyalty += 4
            building.stability += 4
            building.unrest -= 4
            building.law += 2
            building.consumption -= 2
            building.fame -= 1
        elif building.type.name.lower() == 'temple':
            building.loyalty += 2
            building.stability += 2
            building.unrest -= 2
        elif building.type.name.lower() == 'shrine':
            building.loyalty += 1
            building.unrest -= 1
    elif building.deity.name == "Morwyn":
        if building.type.name.lower() == 'cathedral':
            building.loyalty += 4
            building.stability += 4
            building.unrest -= 4
            building.lore += 3
        elif building.type.name.lower() == 'temple':
            building.lore += 2
            building.stability += 2
            building.unrest -= 2
        elif building.type.name.lower() == 'shrine':
            building.stability += 1
            building.unrest -= 1
    elif building.deity.name == "Tinel":
        if building.type.name.lower() == 'cathedral':
            building.economy += 4
            building.society += 3
            building.unrest -= 4
            building.lore += 3
            building.magic_items += ', 1 rare item'
        elif building.type.name.lower() == 'temple':
            building.economy += 2
            building.lore += 2
            building.unrest -= 2
        elif building.type.name.lower() == 'shrine':
            building.economy += 1
            building.unrest -= 1
    elif building.deity.name == "Terak":
        if building.type.name.lower() == 'cathedral':
            building.loyalty += 4
            building.stability += 4
            building.unrest -= 4
            building.law += 2
        elif building.type.name.lower() == 'temple':
            building.loyalty += 2
            building.stability += 2
            building.unrest -= 2
        elif building.type.name.lower() == 'shrine':
            building.stability += 1
            building.unrest -= 1
    elif building.deity.name == "Zheenkeef":
        if building.type.name.lower() == 'cathedral':
            building.loyalty += 4
            building.stability += 4
            building.unrest -= 2
            building.corruption += 2
            building.consumption -= 2
        elif building.type.name.lower() == 'temple':
            building.loyalty += 2
            building.economy += 2
            building.unrest -= 2
            building.corruption += 1
        elif building.type.name.lower() == 'shrine':
            building.economy += 1
            building.unrest -= 1
    elif building.deity.name == "Maal":
        if building.type.name.lower() == 'cathedral':
            building.crime -= 2
            building.stability += 4
            building.unrest -= 4
            building.law += 2
        elif building.type.name.lower() == 'temple':
            building.law += 2
            building.stability += 2
            building.crime -= 2
        elif building.type.name.lower() == 'shrine':
            building.stability += 1
            building.unrest -= 1
    elif building.deity.name == "Mormekar":
        if building.type.name.lower() == 'cathedral':
            building.loyalty += 4
            building.stability += 4
            building.unrest -= 4
            building.lore += 2
        elif building.type.name.lower() == 'temple':
            building.loyalty += 2
            building.stability += 2
            building.unrest -= 2
        elif building.type.name.lower() == 'shrine':
            building.loyalty += 1
            building.unrest -= 1
    elif building.deity.name == "Darmon":
        if building.type.name.lower() == 'cathedral':
            building.loyalty += 4
            building.economy += 4
            building.unrest -= 4
            building.corruption += 3
        elif building.type.name.lower() == 'temple':
            building.economy += 2
            building.loyalty += 1
            building.unrest -= 2
            building.corruption += 1
        elif building.type.name.lower() == 'shrine':
            building.economy += 1
            building.unrest -= 1
    elif building.deity.name == "Arwyn":
        if building.type.name.lower() == 'cathedral':
            building.loyalty += 4
            building.economy += 4
            building.unrest -= 4
            building.society += 2
        elif building.type.name.lower() == 'temple':
            building.loyalty += 2
            building.economy += 2
            building.unrest -= 2
        elif building.type.name.lower() == 'shrine':
            building.loyalty += 1
            building.unrest -= 1
    elif building.deity.name == "Korak":
        if building.type.name.lower() == 'cathedral':
            building.economy += 4
            building.productivity += 3
            building.unrest -= 4
            building.law += 3
        elif building.type.name.lower() == 'temple':
            building.economy += 2
            building.productivity += 2
            building.unrest -= 2
        elif building.type.name.lower() == 'shrine':
            building.economy += 1
            building.unrest -= 1
    elif building.deity.name == "Anwyn":
        if building.type.name.lower() == 'cathedral':
            building.society += 3
            building.stability += 4
            building.unrest -= 4
            building.productivity += 3
        elif building.type.name.lower() == 'temple':
            building.society += 2
            building.stability += 2
            building.unrest -= 2
        elif building.type.name.lower() == 'shrine':
            building.stability += 1
            building.unrest -= 1
    elif building.deity.name == "Canelle":
        if building.type.name.lower() == 'cathedral':
            building.productivity += 3
            building.stability += 4
            building.unrest -= 4
            building.crime += 2
        elif building.type.name.lower() == 'temple':
            building.productivity += 2
            building.stability += 2
            building.unrest -= 2
        elif building.type.name.lower() == 'shrine':
            building.stability += 1
            building.unrest -= 1
    elif building.deity.name == "Naryne":
        if building.type.name.lower() == 'cathedral':
            building.loyalty += 4
            building.economy += 4
            building.unrest -= 4
            building.law += 3
        elif building.type.name.lower() == 'temple':
            building.economy += 2
            building.law += 2
            building.unrest -= 2
        elif building.type.name.lower() == 'shrine':
            building.economy += 1
            building.unrest -= 1
    elif building.deity.name == "Thellyne":
        if building.type.name.lower() == 'cathedral':
            building.loyalty += 4
            building.stability += 4
            building.unrest -= 4
            building.society -= 3
            building.consumption -= 2
        elif building.type.name.lower() == 'temple':
            building.loyalty += 2
            building.stability += 2
            building.unrest -= 2
            building.society -= 1
        elif building.type.name.lower() == 'shrine':
            building.loyalty += 1
            building.unrest -= 1
    return {}
