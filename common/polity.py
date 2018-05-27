from polity.models import Polity
from collections import OrderedDict


class PolityAttribute:
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.source_summary = ""
        self.from_leadership = 0

    def get_total(self):
        self.total = self.from_leadership
        sources = []
        if self.from_leadership != 0:
            sources.append("%s from leadership" % self.from_leadership)
        self.source_summary = ", ".join(sources)

def get_polity_details(id):
    polity = Polity.objects.get(id=id)

    # determine attributes
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
    polity.population = 0
    polity.size = 0
    polity.control_dc = 0

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

    # apply leadership modifiers
    apply_leadership_modifiers(polity)

    # apply terrain modifiers
    apply_terrain_modifiers(polity)

    # apply settlement modifiers
    apply_settlement_modifiers(polity)

    # determine control dc
    polity.control_dc = 20 + polity.size  # + num_districts in all settlements

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

    return {'polity': polity}


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
