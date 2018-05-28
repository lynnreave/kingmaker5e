from settlements.models import Type


def get_settlement_details(settlement):
    # determine buildings
    settlement.buildings = settlement.building.all()
    # determine number of lots
    settlement.lots = 0
    for building in settlement.buildings:
        if building.lots is None:
            settlement.lots += building.type.lots
        else:
            settlement.lots += building.lots
    # determine type
    if settlement.districts > 0:
        settlement.type = Type.objects.get(name="Metropolis")
    elif settlement.lots > 16:
        settlement.type = Type.objects.get(name="City")
    elif settlement.lots > 4:
        settlement.type = Type.objects.get(name="Town")
    else:
        settlement.type = Type.objects.get(name="Village")
    return {}


def get_building_details(building):
    # effects summary
    building.effects_summary = building.type.get_effects_summary()
    return {}
