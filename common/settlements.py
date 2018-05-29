import math
from settlements.models import Type


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

    # apply building modifiers
    for building in settlement.buildings:
        get_building_details(building)
        # lots
        if building.lots is None:
            settlement.lots += building.type.lots
        else:
            settlement.lots += building.lots
        # attributes
        settlement.population += building.type.pop_bonus
        settlement.danger += building.type.dan_bonus
        settlement.economy += building.type.eco_bonus
        settlement.loyalty += building.type.loy_bonus
        settlement.stability += building.type.sta_bonus
        settlement.fame += building.type.fam_bonus
        settlement.infamy += building.type.inf_bonus
        settlement.corruption += building.type.cor_bonus
        settlement.crime += building.type.cri_bonus
        settlement.law += building.type.law_bonus
        settlement.lore += building.type.lor_bonus
        settlement.productivity += building.type.pro_bonus
        settlement.society += building.type.soc_bonus
        settlement.defense += building.type.def_bonus
        settlement.consumption += building.type.con_bonus
        settlement.income += building.type.inc_bonus
        settlement.unrest += building.type.unr_bonus

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
    settlement.consumption = math.floor(settlement.consumption + settlement.type.con_bonus)
    settlement.population = math.floor(settlement.population * settlement.type.pop_mult)
    settlement.danger += settlement.type.dan_mod

    # summary
    attributes = []
    t = 0
    if settlement.population != t: attributes.append('pop %s' % settlement.population)
    if settlement.danger != t: attributes.append('danger %s' % settlement.danger)
    if settlement.economy != t: attributes.append('economy %s' % settlement.economy)
    if settlement.loyalty != t: attributes.append('loyalty %s' % settlement.loyalty)
    if settlement.stability != t: attributes.append('stability %s' % settlement.stability)
    if settlement.fame != t: attributes.append('fame %s' % settlement.fame)
    if settlement.infamy != t: attributes.append('infamy %s' % settlement.infamy)
    if settlement.corruption != t: attributes.append('corruption %s' % settlement.corruption)
    if settlement.crime != t: attributes.append('crime %s' % settlement.crime)
    if settlement.law != t: attributes.append('law %s' % settlement.law)
    if settlement.lore != t: attributes.append('lore %s' % settlement.lore)
    if settlement.productivity != t:
        attributes.append('productivity %s' % settlement.productivity)
    if settlement.society != t: attributes.append('society %s' % settlement.society)
    if settlement.defense != t: attributes.append('defense %s' % settlement.defense)
    if settlement.consumption != t: attributes.append('consumption %s' % settlement.consumption)
    if settlement.income != t: attributes.append('income %s' % settlement.income)
    if settlement.unrest != t: attributes.append('unrest %s' % settlement.unrest)
    settlement.att_summary = ', '.join(attributes)

    return {}


def get_building_details(building):
    # effects summary
    building.effects_summary = building.type.get_effects_summary()
    return {}
