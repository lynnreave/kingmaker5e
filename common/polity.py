from polity.models import Polity
from .territory import get_territory_effects
from .utils import get_signed_number
from .settlements import get_settlement_details
import math


class PolityAttribute:
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.total_dice = ""
        self.dice = []
        self.source_summary = ""
        self.from_government = 0
        self.from_alignment = 0
        self.from_edicts = 0
        self.from_edicts_dice = []
        self.from_leadership = 0
        self.from_terrain = 0
        self.from_diplomacy = 0
        self.from_settlements = 0

        self.from_events = 0

    def get_total(self):
        self.total = 0 \
            + self.from_government \
            + self.from_alignment \
            + self.from_leadership \
            + self.from_terrain \
            + self.from_settlements \
            + self.from_edicts \
            + self.from_diplomacy \
            + self.from_events
        self.total = math.floor(self.total)
        if len(self.dice) > 0:
            self.total_dice = ' + ' + " + ".join(self.dice)

        sources = []
        if self.from_government != 0:
            sources.append("%s from government" % get_signed_number(self.from_government)['s'])
        if self.from_alignment != 0:
            sources.append("%s from alignment" % get_signed_number(self.from_alignment)['s'])
        if self.from_edicts != 0 or len(self.from_edicts_dice) > 0:
            s = ''
            if self.from_edicts != 0: s += ' %s' % get_signed_number(self.from_edicts)['s']
            if len(self.from_edicts_dice) > 0:
                s += ' + ' + " + ".join(self.from_edicts_dice)
            sources.append(s + ' from edicts')
        if self.from_leadership != 0:
            sources.append("%s from leadership" % get_signed_number(self.from_leadership)['s'])
        if self.from_terrain != 0:
            sources.append("%s from terrain" % get_signed_number(self.from_terrain)['s'])
        if self.from_settlements != 0:
            sources.append("%s from settlements" % get_signed_number(self.from_settlements)['s'])
        if self.from_diplomacy != 0:
            sources.append("%s from diplomacy" % get_signed_number(self.from_diplomacy)['s'])

        if self.from_events != 0:
            sources.append("%s from events" % get_signed_number(self.from_events)['s'])
        self.source_summary = ", ".join(sources)


def get_polity_details(id):
    polity = Polity.objects.get(id=id)

    # define attributes
    # define major attributes
    polity.economy = PolityAttribute('economy')
    polity.loyalty = PolityAttribute('loyalty')
    polity.stability = PolityAttribute('stability')
    # define minor attributes
    polity.fame = PolityAttribute('fame')
    polity.infamy = PolityAttribute('infamy')
    polity.corruption = PolityAttribute('corruption')
    polity.crime = PolityAttribute('crime')
    polity.law = PolityAttribute('law')
    polity.lore = PolityAttribute('lore')
    polity.productivity = PolityAttribute('productivity')
    polity.society = PolityAttribute('society')
    # define other attributes
    polity.population = PolityAttribute('population')
    polity.size = PolityAttribute('size')
    polity.control_dc = 0
    polity.income = PolityAttribute('income')
    polity.defense = PolityAttribute('defense')
    polity.unrest_mod = PolityAttribute('unrest')
    polity.consumption = PolityAttribute('consumption')

    # determine roles
    # define roles
    polity.ruler = None
    polity.co_ruler = None
    polity.consort = None
    polity.councilor = None
    polity.general = None
    polity.grand_diplomat = None
    polity.heir = None
    polity.high_priest = None
    polity.magister = None
    polity.marshal = None
    polity.royal_enforcer = None
    polity.spymaster = None
    polity.treasurer = None
    polity.viceroy = None
    polity.warden = None
    # determine person in each role
    determine_polity_leadership_roles(polity)

    # determine attribute values
    # apply alignment bonuses
    apply_alignment_modifiers(polity)
    # apply government bonuses
    apply_government_modifiers(polity)
    # apply edict modifiers
    apply_edict_modifiers(polity)
    # apply terrain modifiers
    apply_terrain_modifiers(polity)
    # apply leadership modifiers
    apply_leadership_modifiers(polity)
    # apply diplomacy modifiers
    apply_diplomacy_modifiers(polity)
    # apply settlement modifiers
    apply_settlement_modifiers(polity)
    # apply military modifiers
    apply_military_modifiers(polity)
    # apply event modifiers
    apply_event_modifiers(polity)
    # calculate total major attributes
    polity.economy.get_total()
    polity.loyalty.get_total()
    polity.stability.get_total()
    # calculate total minor attributes
    polity.fame.get_total()
    polity.infamy.get_total()
    polity.corruption.get_total()
    polity.crime.get_total()
    polity.law.get_total()
    polity.lore.get_total()
    polity.productivity.get_total()
    polity.society.get_total()
    # calculate total misc attributes
    polity.population.get_total()
    polity.size.get_total()
    polity.income.get_total()
    polity.defense.get_total()
    polity.unrest_mod.get_total()
    polity.consumption.get_total()
    # calculate control dc
    polity.control_dc = 20 + polity.size.total  # + num_districts in all settlements

    return {'polity': polity}


def apply_alignment_modifiers(polity):
    polity.economy.from_alignment += polity.alignment_lc.eco_bonus + polity.alignment_ge.eco_bonus
    polity.loyalty.from_alignment += polity.alignment_lc.loy_bonus + polity.alignment_ge.loy_bonus
    polity.stability.from_alignment \
        += polity.alignment_lc.sta_bonus + polity.alignment_ge.sta_bonus
    polity.fame.from_alignment += polity.alignment_lc.fam_bonus + polity.alignment_ge.fam_bonus
    polity.infamy.from_alignment += polity.alignment_lc.inf_bonus + polity.alignment_ge.inf_bonus
    polity.corruption.from_alignment \
        += polity.alignment_lc.cor_bonus + polity.alignment_ge.cor_bonus
    polity.crime.from_alignment += polity.alignment_lc.cri_bonus + polity.alignment_ge.cri_bonus
    polity.law.from_alignment += polity.alignment_lc.law_bonus + polity.alignment_ge.law_bonus
    polity.lore.from_alignment += polity.alignment_lc.lor_bonus + polity.alignment_ge.lor_bonus
    polity.productivity.from_alignment \
        += polity.alignment_lc.pro_bonus + polity.alignment_ge.pro_bonus
    polity.society.from_alignment += polity.alignment_lc.soc_bonus + polity.alignment_ge.soc_bonus
    return {}


def apply_diplomacy_modifiers(polity):
    diplomatic_relations = polity.diplomatic_relation.all()
    for diplomatic_relation in diplomatic_relations:
        for treaty in diplomatic_relation.treaties.all():
            polity.economy.from_diplomacy += (
                    treaty.eco_mult * diplomatic_relation.economy
            )
            polity.stability.from_diplomacy += (
                    treaty.sta_mult * diplomatic_relation.stability
            )
    return {}


def apply_edict_modifiers(polity):
    # tax edict
    polity.economy.from_edicts += polity.tax_edict.eco_bonus
    polity.loyalty.from_edicts += polity.tax_edict.loy_bonus
    # promotion edict
    polity.economy.from_edicts += polity.promotion_edict.eco_bonus
    polity.loyalty.from_edicts += polity.promotion_edict.loy_bonus
    polity.stability.from_edicts += polity.promotion_edict.sta_bonus
    if polity.promotion_edict.con_dice is not None:
        dice_s = 'd'.join(
            [str(polity.promotion_edict.con_bonus), str(polity.promotion_edict.con_dice)]
        )
        polity.consumption.dice.append(dice_s)
        polity.consumption.from_edicts_dice.append(dice_s)
    else:
        polity.consumption.from_edicts += polity.promotion_edict.con_bonus
    # holiday edict
    polity.economy.from_edicts += polity.holiday_edict.eco_bonus
    polity.loyalty.from_edicts += polity.holiday_edict.loy_bonus
    if polity.holiday_edict.con_dice is not None:
        dice_s = 'd'.join(
            [str(polity.holiday_edict.con_bonus), str(polity.holiday_edict.con_dice)]
        )
        polity.consumption.dice.append(dice_s)
        polity.consumption.from_edicts_dice.append(dice_s)
    else:
        polity.consumption.from_edicts += polity.holiday_edict.con_bonus
    # recruitment edict
    polity.fame.from_edicts += polity.recruitment_edict.fam_bonus
    polity.infamy.from_edicts += polity.recruitment_edict.inf_bonus
    polity.defense.from_edicts += polity.recruitment_edict.def_bonus
    polity.economy.from_edicts += polity.recruitment_edict.eco_bonus
    polity.society.from_edicts += polity.recruitment_edict.soc_bonus
    return {}


def apply_event_modifiers(polity):
    events = polity.event.all()
    for event in events:
        polity.economy.from_events += event.eco_bonus
        polity.loyalty.from_events += event.loy_bonus
        polity.stability.from_events += event.sta_bonus
        polity.fame.from_events += event.fam_bonus
        polity.infamy.from_events += event.inf_bonus
        polity.corruption.from_events += event.cor_bonus
        polity.crime.from_events += event.cri_bonus
        polity.law.from_events += event.law_bonus
        polity.lore.from_events += event.lor_bonus
        polity.productivity.from_events += event.pro_bonus
        polity.society.from_events += event.soc_bonus
        polity.defense.from_events += event.def_bonus
        polity.consumption.from_events += event.con_bonus
        polity.income.from_events += event.inc_bonus
        polity.unrest_mod.from_events += event.unr_bonus
    return {}


def apply_government_modifiers(polity):
    polity.economy.from_government += polity.government.eco_bonus
    polity.loyalty.from_government += polity.government.loy_bonus
    polity.stability.from_government += polity.government.sta_bonus
    polity.fame.from_government += polity.government.fam_bonus
    polity.infamy.from_government += polity.government.inf_bonus
    polity.corruption.from_government += polity.government.cor_bonus
    polity.crime.from_government += polity.government.cri_bonus
    polity.law.from_government += polity.government.law_bonus
    polity.lore.from_government += polity.government.lor_bonus
    polity.productivity.from_government += polity.government.pro_bonus
    polity.society.from_government += polity.government.soc_bonus
    return {}


def apply_leadership_modifiers(polity):
    # ruler
    # determine mod
    if polity.ruler is not None:
        ruler_mod = polity.ruler.leadership_mod
    elif polity.co_ruler is not None:
        ruler_mod = polity.co_ruler.leadership_mod
    else:
        ruler_mod = 0
    # update attribute
    if polity.ruler_attribute_1 is not None:
        if polity.ruler_attribute_1.name.lower() == 'economy':
            polity.economy.from_leadership += ruler_mod
        elif polity.ruler_attribute_1.name.lower() == 'loyalty':
            polity.loyalty.from_leadership += ruler_mod
        elif polity.ruler_attribute_1.name.lower() == 'stability':
            polity.stability.from_leadership += ruler_mod
    if polity.ruler_attribute_2 is not None and polity.size > 25:
        if polity.ruler_attribute_2.name.lower() == 'economy':
            polity.economy.from_leadership += ruler_mod
        elif polity.ruler_attribute_2.name.lower() == 'loyalty':
            polity.loyalty.from_leadership += ruler_mod
        elif polity.ruler_attribute_2.name.lower() == 'stability':
            polity.stability.from_leadership += ruler_mod
    if polity.ruler_attribute_3 is not None and polity.size > 100:
        if polity.ruler_attribute_3.name.lower() == 'economy':
            polity.economy.from_leadership += ruler_mod
        elif polity.ruler_attribute_3.name.lower() == 'loyalty':
            polity.loyalty.from_leadership += ruler_mod
        elif polity.ruler_attribute_3.name.lower() == 'stability':
            polity.stability.from_leadership += ruler_mod

    # consort
    if polity.consort is not None:
        polity.loyalty.from_leadership += (polity.consort.leadership_mod / 2)

    # councilor
    if polity.councilor is not None:
        polity.loyalty.from_leadership += polity.councilor.leadership_mod

    # general
    if polity.general is not None:
        polity.stability.from_leadership += polity.general.leadership_mod

    # grand_diplomat
    if polity.grand_diplomat is not None:
        polity.stability.from_leadership += polity.grand_diplomat.leadership_mod

    # heir
    if polity.heir is not None:
        polity.loyalty.from_leadership += (polity.heir.leadership_mod / 2)

    # high_priest
    if polity.high_priest is not None:
        polity.stability.from_leadership += polity.high_priest.leadership_mod

    # magister
    if polity.magister is not None:
        polity.economy.from_leadership += polity.magister.leadership_mod

    # marshal
    if polity.marshal is not None:
        polity.economy.from_leadership += polity.marshal.leadership_mod

    # royal_enforcer
    if polity.royal_enforcer is not None:
        polity.loyalty.from_leadership += polity.royal_enforcer.leadership_mod

    # spymaster
    if polity.spymaster is not None:
        if polity.spymaster_attribute.name.lower() == 'economy':
            polity.economy.from_leadership += polity.spymaster.leadership_mod
        elif polity.spymaster_attribute.name.lower() == 'loyalty':
            polity.loyalty.from_leadership += polity.spymaster.leadership_mod
        elif polity.spymaster_attribute.name.lower() == 'stability':
            polity.stability.from_leadership += polity.spymaster.leadership_mod

    # treasurer
    if polity.treasurer is not None:
        polity.economy.from_leadership += polity.treasurer.leadership_mod

    # viceroy
    if polity.viceroy is not None:
        polity.economy.from_leadership += (polity.viceroy.leadership_mod / 2)

    # warden
    if polity.warden is not None:
        polity.loyalty.from_leadership += polity.warden.leadership_mod
    return {}


def apply_military_modifiers(polity):
    return {}


def apply_settlement_modifiers(polity):
    # get all settlements for polity
    territories = polity.territory.all()
    polity.settlements = []
    for territory in territories:
        settlements = territory.settlement.all()
        if len(settlements) > 0:
            for settlement in settlements:
                polity.settlements.append(get_settlement_details(settlement)['settlement'])
    # apply modifiers
    for settlement in polity.settlements:
        polity.size.from_settlements += settlement.districts
        polity.population.from_settlements += settlement.population
        # economy
        bonus = 0
        if settlement.economy > 0:
            bonus = settlement.economy + settlement.type.att_mod
            if bonus < 0: bonus = 0
        elif settlement.economy < 0:
            bonus = settlement.economy - settlement.type.att_mod
            if bonus > 0: bonus = 0
        if bonus != 0: polity.economy.from_settlements += bonus
        # loyalty
        bonus = 0
        if settlement.loyalty > 0:
            bonus = settlement.loyalty + settlement.type.att_mod
            if bonus < 0: bonus = 0
        elif settlement.loyalty < 0:
            bonus = settlement.loyalty - settlement.type.att_mod
            if bonus > 0: bonus = 0
        if bonus != 0: polity.loyalty.from_settlements += bonus
        # stability
        bonus = 0
        if settlement.stability > 0:
            bonus = settlement.stability + settlement.type.att_mod
            if bonus < 0: bonus = 0
        elif settlement.stability < 0:
            bonus = settlement.stability - settlement.type.att_mod
            if bonus > 0: bonus = 0
        if bonus != 0: polity.stability.from_settlements += bonus
        # fame
        bonus = 0
        if settlement.fame > 0:
            bonus = settlement.fame + settlement.type.att_mod
            if bonus < 0: bonus = 0
        elif settlement.fame < 0:
            bonus = settlement.fame - settlement.type.att_mod
            if bonus > 0: bonus = 0
        if bonus != 0: polity.fame.from_settlements += bonus
        # infamy
        bonus = 0
        if settlement.infamy > 0:
            bonus = settlement.infamy + settlement.type.att_mod
            if bonus < 0: bonus = 0
        elif settlement.infamy < 0:
            bonus = settlement.infamy - settlement.type.att_mod
            if bonus > 0: bonus = 0
        if bonus != 0: polity.infamy.from_settlements += bonus
        # corruption
        bonus = 0
        if settlement.corruption > 0:
            bonus = settlement.corruption + settlement.type.att_mod
            if bonus < 0: bonus = 0
        elif settlement.corruption < 0:
            bonus = settlement.corruption - settlement.type.att_mod
            if bonus > 0: bonus = 0
        if bonus != 0: polity.corruption.from_settlements += bonus
        # crime
        bonus = 0
        if settlement.crime > 0:
            bonus = settlement.crime + settlement.type.att_mod
            if bonus < 0: bonus = 0
        elif settlement.crime < 0:
            bonus = settlement.crime - settlement.type.att_mod
            if bonus > 0: bonus = 0
        if bonus != 0: polity.crime.from_settlements += bonus
        # law
        bonus = 0
        if settlement.law > 0:
            bonus = settlement.law + settlement.type.att_mod
            if bonus < 0: bonus = 0
        elif settlement.law < 0:
            bonus = settlement.law - settlement.type.att_mod
            if bonus > 0: bonus = 0
        if bonus != 0: polity.law.from_settlements += bonus
        # lore
        bonus = 0
        if settlement.lore > 0:
            bonus = settlement.lore + settlement.type.att_mod
            if bonus < 0: bonus = 0
        elif settlement.lore < 0:
            bonus = settlement.lore - settlement.type.att_mod
            if bonus > 0: bonus = 0
        if bonus != 0: polity.lore.from_settlements += bonus
        # productivity
        bonus = 0
        if settlement.productivity > 0:
            bonus = settlement.productivity + settlement.type.att_mod
            if bonus < 0: bonus = 0
        elif settlement.productivity < 0:
            bonus = settlement.productivity - settlement.type.att_mod
            if bonus > 0: bonus = 0
        if bonus != 0: polity.productivity.from_settlements += bonus
        # society
        bonus = 0
        if settlement.society > 0:
            bonus = settlement.society + settlement.type.att_mod
            if bonus < 0: bonus = 0
        elif settlement.society < 0:
            bonus = settlement.society - settlement.type.att_mod
            if bonus > 0: bonus = 0
        if bonus != 0: polity.society.from_settlements += bonus
        # other
        polity.defense.from_settlements += settlement.defense
        polity.consumption.from_settlements += settlement.consumption
        polity.income.from_settlements += settlement.income
    return {}


def apply_terrain_modifiers(polity):
    territories = polity.territory.all()
    get_territory_effects(territories)
    for territory in territories:
        polity.population.from_terrain += territory.pop_bonus
        polity.economy.from_terrain += territory.eco_bonus
        polity.loyalty.from_terrain += territory.loy_bonus
        polity.stability.from_terrain += territory.sta_bonus
        polity.fame.from_terrain += territory.fam_bonus
        polity.infamy.from_terrain += territory.inf_bonus
        polity.corruption.from_terrain += territory.cor_bonus
        polity.crime.from_terrain += territory.cri_bonus
        polity.law.from_terrain += territory.law_bonus
        polity.lore.from_terrain += territory.lor_bonus
        polity.productivity.from_terrain += territory.pro_bonus
        polity.society.from_terrain += territory.soc_bonus
        polity.defense.from_terrain += territory.def_bonus
        polity.consumption.from_terrain += territory.con_bonus
        polity.income.from_terrain += territory.inc_bonus
    polity.size.from_terrain += len(territories)
    return {}


def determine_polity_leadership_roles(polity):
    citizens = polity.person.order_by('leadership_role__ranking', 'leadership_role__name')
    polity.leadership = []
    for person in citizens:
        role = person.leadership_role.name.lower()
        if role == 'ruler':
            polity.ruler = person
            polity.ruler.leadership_mod = get_ability_score_mod(polity.ruler.cha)['mod']
        elif role == 'co-ruler':
            polity.co_ruler = person
            polity.co_ruler.leadership_mod = get_ability_score_mod(polity.co_ruler.cha)['mod']
        elif role == 'consort':
            polity.consort = person
            polity.consort.leadership_mod = get_ability_score_mod(polity.consort.cha)['mod']
        elif role == 'councilor':
            polity.councilor = person
            if polity.councilor.cha > polity.councilor.wis:
                polity.councilor.leadership_mod = get_ability_score_mod(
                    polity.councilor.cha
                )['mod']
            else:
                polity.councilor.leadership_mod = get_ability_score_mod(
                    polity.councilor.wis
                )['mod']
        elif role == 'general':
            polity.general = person
            if polity.general.cha > polity.general.str:
                polity.general.leadership_mod = get_ability_score_mod(
                    polity.general.cha
                )['mod']
            else:
                polity.general.leadership_mod = get_ability_score_mod(
                    polity.general.str
                )['mod']
        elif role == 'grand diplomat':
            polity.grand_diplomat = person
            if polity.grand_diplomat.cha > polity.grand_diplomat.int:
                polity.grand_diplomat.leadership_mod = get_ability_score_mod(
                    polity.grand_diplomat.cha
                )['mod']
            else:
                polity.grand_diplomat.leadership_mod = get_ability_score_mod(
                    polity.grand_diplomat.int
                )['mod']
        elif role == 'heir':
            polity.heir = person
            polity.heir.leadership_mod = get_ability_score_mod(polity.heir.cha)['mod']
        elif role == 'high priest':
            polity.high_priest = person
            if polity.high_priest.cha > polity.high_priest.wis:
                polity.high_priest.leadership_mod = get_ability_score_mod(
                    polity.high_priest.cha
                )['mod']
            else:
                polity.high_priest.leadership_mod = get_ability_score_mod(
                    polity.high_priest.wis
                )['mod']
        elif role == 'magister':
            polity.magister = person
            if polity.magister.cha > polity.magister.int:
                polity.magister.leadership_mod = get_ability_score_mod(
                    polity.magister.cha
                )['mod']
            else:
                polity.magister.leadership_mod = get_ability_score_mod(
                    polity.magister.int
                )['mod']
        elif role == 'marshal':
            polity.marshal = person
            if polity.marshal.dex > polity.marshal.wis:
                polity.marshal.leadership_mod = get_ability_score_mod(
                    polity.marshal.dex
                )['mod']
            else:
                polity.marshal.leadership_mod = get_ability_score_mod(
                    polity.marshal.wis
                )['mod']
        elif role == 'royal enforcer':
            polity.royal_enforcer = person
            if polity.royal_enforcer.dex > polity.royal_enforcer.str:
                polity.royal_enforcer.leadership_mod = get_ability_score_mod(
                    polity.royal_enforcer.dex
                )['mod']
            else:
                polity.royal_enforcer.leadership_mod = get_ability_score_mod(
                    polity.royal_enforcer.str
                )['mod']
        elif role == 'spymaster':
            polity.spymaster = person
            if polity.spymaster.dex > polity.spymaster.int:
                polity.spymaster.leadership_mod = get_ability_score_mod(
                    polity.spymaster.dex
                )['mod']
            else:
                polity.spymaster.leadership_mod = get_ability_score_mod(
                    polity.spymaster.int
                )['mod']
        elif role == 'treasurer':
            polity.treasurer = person
            if polity.treasurer.int > polity.treasurer.wis:
                polity.treasurer.leadership_mod = get_ability_score_mod(
                    polity.treasurer.int
                )['mod']
            else:
                polity.treasurer.leadership_mod = get_ability_score_mod(
                    polity.treasurer.wis
                )['mod']
        elif role == 'viceroy':
            polity.viceroy = person
            if polity.viceroy.int > polity.viceroy.wis:
                polity.viceroy.leadership_mod = get_ability_score_mod(
                    polity.viceroy.int
                )['mod']
            else:
                polity.viceroy.leadership_mod = get_ability_score_mod(
                    polity.viceroy.wis
                )['mod']
        elif role == 'warden':
            polity.warden = person
            if polity.warden.con > polity.warden.str:
                polity.warden.leadership_mod = get_ability_score_mod(
                    polity.warden.con
                )['mod']
            else:
                polity.warden.leadership_mod = get_ability_score_mod(
                    polity.warden.str
                )['mod']
        else:
            role = None
        if role is not None:
            polity.leadership.append(person)

    return {}


def get_ability_score_mod(score):
    mod = 0
    if score in [12, 13]: mod = 1
    elif score in [14, 15]: mod = 2
    elif score in [16, 17]: mod = 3
    elif score in [18, 19]: mod = 4
    elif score in [20, 21]: mod = 5
    elif score in [8, 9]: mod = -1
    elif score in [6, 7]: mod = -2
    elif score in [4, 5]: mod = -3
    elif score in [2, 3]: mod = -4
    elif score in [1]: mod = -5
    elif score in [22, 23]: mod = 6
    elif score in [24, 25]: mod = 7
    elif score in [26, 27]: mod = 8
    return {'mod': mod}
