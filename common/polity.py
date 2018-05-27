from polity.models import Polity


class PolityAttribute:
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.source_summary = ""
        self.from_government = 0
        self.from_alignment = 0
        self.from_leadership = 0

    def get_total(self):
        self.total = 0 \
            + self.from_government \
            + self.from_alignment \
            + self.from_leadership
        sources = []
        if self.from_government > 0:
            sources.append("+%s from government" % self.from_government)
        elif self.from_government < 0:
            sources.append("-%s from government" % self.from_government)
        if self.from_alignment > 0:
            sources.append("+%s from alignment" % self.from_alignment)
        elif self.from_alignment < 0:
            sources.append("-%s from alignment" % self.from_alignment)
        if self.from_leadership > 0:
            sources.append("+%s from leadership" % self.from_leadership)
        elif self.from_leadership < 0:
            sources.append("-%s from leadership" % self.from_leadership)
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
    # apply terrain modifiers
    apply_terrain_modifiers(polity)
    # apply leadership modifiers
    apply_leadership_modifiers(polity)
    # apply settlement modifiers
    apply_settlement_modifiers(polity)
    # calculate total attributes
    polity.economy.get_total()
    polity.loyalty.get_total()
    polity.stability.get_total()
    polity.fame.get_total()
    polity.infamy.get_total()
    polity.corruption.get_total()
    polity.crime.get_total()
    polity.law.get_total()
    polity.lore.get_total()
    polity.productivity.get_total()
    polity.society.get_total()
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


def apply_terrain_modifiers(polity):
    return {}


def apply_settlement_modifiers(polity):
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
