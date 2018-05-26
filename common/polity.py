from polity.models import Polity


def get_polity_details(id):
    polity = Polity.objects.get(id=id)
    # determine roles
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
    citizens = polity.person.order_by('leadership_role__ranking', 'leadership_role__name')
    polity.leadership = []
    for person in citizens:
        role = person.leadership_role.name.lower()
        if role == 'ruler': polity.ruler = person
        elif role == 'co-ruler': polity.co_ruler = person
        elif role == 'consort': polity.consort = person
        elif role == 'councilor': polity.ruler = person
        elif role == 'general': polity.general = person
        elif role == 'grand diplomat': polity.grand_diplomat = person
        elif role == 'heir': polity.heir = person
        elif role == 'high priest': polity.high_priest = person
        elif role == 'magister': polity.magister = person
        elif role == 'marshal': polity.marshal = person
        elif role == 'royal enforcer': polity.royal_enforcer = person
        elif role == 'spymaster': polity.spymaster = person
        elif role == 'treasurer': polity.treasurer = person
        elif role == 'viceroy': polity.viceroy = person
        elif role == 'warden': polity.warden = person
        else: role = None
        if role is not None: polity.leadership.append(person)

    return {'polity': polity}
