import math
from .utils import get_mixed_number_string, get_signed_number, get_ability_score_mod


def get_armed_force_details(armed_force):
    # define attributes
    armed_force.cr = 0
    armed_force.troop_cr = 0
    armed_force.equip_cost_mult = armed_force.size.equip_cost_mult
    armed_force.camo_mod = armed_force.size.camo_mod
    armed_force.camo_mod_string = get_signed_number(armed_force.size.camo_mod)['s']
    armed_force.equipment_string = ''
    armed_force.commander_boons = ''
    # derived
    armed_force.acr = 0
    armed_force.hp = 0
    armed_force.om_melee = 0
    armed_force.om_ranged = 0
    armed_force.dv = 0
    armed_force.consumption = 0
    armed_force.consumption_weekly = 0
    armed_force.leadership_bonus = 0
    armed_force.leadership_bonus_string = 'None'

    # determine cr
    if armed_force.custom_cr is not None:
        armed_force.troop_cr = armed_force.custom_cr
    else:
        armed_force.troop_cr = armed_force.type.default_cr
    # mount vs. troop
    armed_force.cr = armed_force.troop_cr
    if armed_force.mount_cr is not None:
        if armed_force.mount_cr > armed_force.troop_cr:
            armed_force.cr = armed_force.mount_cr

    # determine acr
    armed_force.acr = determine_acr(armed_force.cr, armed_force.size.acr_mod)

    # hp
    # get hit die string
    armed_force.hd_string = "1d%s" % armed_force.hit_die
    # get hp for unit
    armed_force.hp = math.floor(((armed_force.hit_die / 2) + 0.5) * armed_force.acr)

    # offense modifier & defense value
    armed_force.om_melee = math.floor(armed_force.acr)
    if armed_force.mount_cr is not None:
        armed_force.om_ranged = math.floor(
            determine_acr(armed_force.troop_cr, armed_force.size.acr_mod)
        )
    else:
        armed_force.om_ranged = math.floor(armed_force.acr)
    armed_force.dv = math.floor(10 + armed_force.acr)

    # consumption
    armed_force.consumption_weekly = math.floor(armed_force.acr / 2)
    if armed_force.consumption_weekly < 1: armed_force.consumption_weekly = 1
    if armed_force.active:
        armed_force.consumption = 4 * armed_force.consumption_weekly
    else:
        armed_force.consumption = armed_force.consumption_weekly

    # determine leadership bonus
    if armed_force.commander is not None:
        armed_force.leadership_bonus = math.floor(armed_force.commander.hit_dice / 5) + \
            get_ability_score_mod(armed_force.commander.cha)['mod']
        if get_ability_score_mod(armed_force.commander.cha)['mod'] >= 3:
            armed_force.leadership_bonus += 1
        if get_ability_score_mod(armed_force.commander.wis)['mod'] >= 3:
            armed_force.leadership_bonus += 1
        if get_ability_score_mod(armed_force.commander.int)['mod'] >= 3:
            armed_force.leadership_bonus += 1
        armed_force.leadership_bonus_string = get_signed_number(armed_force.leadership_bonus)['s']

    # determine commander boons
        boons = []
        for boon in armed_force.commander.boons.all():
            boons.append(boon.name)
        armed_force.commander_boons = ', '.join(boons)

    # apply equipment modifiers
    eqt = []
    for item in armed_force.equipment.all():
        get_equipment_details(item)
        eqt.append(item.name)
        armed_force.om_melee += item.om_melee_mod + item.om_mod
        armed_force.om_ranged += item.om_ranged_mod + item.om_mod
        armed_force.dv += item.dv_mod
        armed_force.speed += item.speed_mod
        armed_force.morale += item.morale_mod
    armed_force.equipment_string = ', '.join(eqt)

    # tactics
    tactics_known = []
    for tactic in armed_force.tactics_known.all():
        tactics_known.append(tactic.name)
    armed_force.tactics_known_string = ', '.join(tactics_known)

    # special abilities
    abilities = []
    for ability in armed_force.special_abilities.all():
        abilities.append(ability.name)
    armed_force.special_abilities_string = ', '.join(abilities)

    # summaries
    armed_force.cr_string = get_mixed_number_string(armed_force.cr)
    armed_force.acr_string = get_mixed_number_string(armed_force.acr)
    armed_force.om_melee_string = get_signed_number(armed_force.om_melee)['s']
    armed_force.om_ranged_string = get_signed_number(armed_force.om_ranged)['s']
    armed_force.om_string = "%s/%s" % (armed_force.om_melee_string, armed_force.om_ranged_string)

    return {'armed force': armed_force}


def determine_acr(cr, acr_mod):
    steps = acr_mod
    acr = cr
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
    return acr


def get_equipment_details(equipment):
    # requirements
    reqs = []
    for requirement in equipment.requirements.all():
        reqs.append(requirement.name)
    equipment.requirements_string = ', '.join(reqs)

    # offense mod
    equipment.om_melee_mod_string = get_signed_number(equipment.om_melee_mod + equipment.om_mod)['s']
    equipment.om_ranged_mod_string = get_signed_number(equipment.om_ranged_mod + equipment.om_mod)['s']
    equipment.om_mod_string = "%s/%s" % (equipment.om_melee_mod_string, equipment.om_ranged_mod_string)

    # defense mod
    equipment.dv_mod_string = get_signed_number(equipment.dv_mod)['s']

    # speed mod
    equipment.speed_mod_string = get_signed_number(equipment.speed_mod)['s']

    # morale mod
    equipment.morale_mod_string = get_signed_number(equipment.morale_mod)['s']

    return {'equipment': equipment}
