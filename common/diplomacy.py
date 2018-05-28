from .polity import get_polity_details, math


def get_diplomacy_dcs(diplomatic_relations):
    for diplomatic_relation in diplomatic_relations:
        polity = get_polity_details(diplomatic_relation.holder.id)['polity']
        diplomatic_relation.dc = math.floor(
            5 + polity.infamy.total + (diplomatic_relation.size / 5)
            + (polity.size.total / 5) - diplomatic_relation.attitude.step - polity.fame.total
        )
    return {}
