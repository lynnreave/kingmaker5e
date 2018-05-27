from polity.models import Polity
from collections import OrderedDict


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
    polity.treasury = 0
    polity.income = PolityAttribute('income')
    polity.defense = PolityAttribute('defense')
    polity.unrest = PolityAttribute('unrest')
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
    # apply leadership modifiers
    apply_leadership_modifiers(polity)
    # apply terrain modifiers
    apply_terrain_modifiers(polity)
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
    return {}


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
        elif role == 'co-ruler':
            polity.co_ruler = person
        elif role == 'consort':
            polity.consort = person
        elif role == 'councilor':
            polity.ruler = person
        elif role == 'general':
            polity.general = person
        elif role == 'grand diplomat':
            polity.grand_diplomat = person
        elif role == 'heir':
            polity.heir = person
        elif role == 'high priest':
            polity.high_priest = person
        elif role == 'magister':
            polity.magister = person
        elif role == 'marshal':
            polity.marshal = person
        elif role == 'royal enforcer':
            polity.royal_enforcer = person
        elif role == 'spymaster':
            polity.spymaster = person
        elif role == 'treasurer':
            polity.treasurer = person
        elif role == 'viceroy':
            polity.viceroy = person
        elif role == 'warden':
            polity.warden = person
        else:
            role = None
        if role is not None:
            polity.leadership.append(person)

    return {}
