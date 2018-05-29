import math
from .utils import get_mixed_number_string, get_signed_number


def get_armed_force_details(armed_force):
    # define attributes
    armed_force.cr = 0
    armed_force.equip_cost_mult = armed_force.size.equip_cost_mult
    armed_force.camo_mod = armed_force.size.camo_mod
    armed_force.camo_mod_string = get_signed_number(armed_force.size.camo_mod)['s']
    # derived
    armed_force.acr = 0
    armed_force.hp = 0
    armed_force.om = 0
    armed_force.dv = 0
    armed_force.consumption = 0
    armed_force.consumption_weekly = 0

    # determine cr
    if armed_force.custom_cr is not None:
        armed_force.cr = armed_force.custom_cr
    else:
        armed_force.cr = armed_force.type.default_cr
    # express as fraction if fraction
    armed_force.cr_string = get_mixed_number_string(armed_force.cr)

    # determine acr
    steps = armed_force.size.acr_mod
    acr = armed_force.cr
    while steps != 0:
        if steps > 0 and acr >= 1:
            acr += steps
            break
        elif steps < 0 and ((acr + steps) >= 1):
            acr += steps
            break
        elif steps > 0 and acr < 1:
            steps -= 1
            acr = acr * 2
        elif steps < 0 and ((acr - 1) >= 1):
            steps += 1
            acr -= 1
        elif steps < 0 and acr > 0.125:
            steps += 1
            acr = acr/2
        elif steps == 0:
            break
        else:
            acr = 0
            break
    armed_force.acr = acr
    armed_force.acr_string = get_mixed_number_string(armed_force.acr)

    # hp
    # get hit die string
    armed_force.hd_string = "1d%s" % armed_force.hit_die
    # get hp for unit
    armed_force.hp = math.floor(((armed_force.hit_die / 2) + 0.5) * armed_force.acr)

    # offense modifier & defense value
    armed_force.om = math.floor(armed_force.acr)
    armed_force.om_string = get_signed_number(armed_force.om)['s']
    armed_force.dv = math.floor(10 + armed_force.acr)

    # consumption
    armed_force.consumption_weekly = math.floor(armed_force.acr / 2)
    if armed_force.consumption_weekly < 1: armed_force.consumption_weekly = 1
    armed_force.consumption = 4 * armed_force.consumption_weekly

    return {'armed force': armed_force}
