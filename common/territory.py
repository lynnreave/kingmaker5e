

def get_territory_effects(territories):
    for territory in territories:
        # set base by type of terrain
        territory.pop_bonus = territory.type.pop_bonus
        territory.dan_bonus = territory.type.dan_bonus
        territory.eco_bonus = 0
        territory.loy_bonus = 0
        territory.sta_bonus = 0
        territory.def_bonus = 0
        territory.con_bonus = 0
        territory.inc_bonus = 0
        territory.unr_bonus = 0
        # special vars
        has_lair = False
        has_watchtower = False
        has_fort = False
        has_landmark = False
        has_road = False
        has_highway = False
        has_resource = False
        has_farm = False
        has_fishery = False
        improvements = []
        # add bonuses from each improvement
        for improvement in territory.improvements.all():
            territory.pop_bonus += improvement.pop_bonus
            territory.eco_bonus += improvement.eco_bonus
            territory.loy_bonus += improvement.loy_bonus
            territory.sta_bonus += improvement.sta_bonus
            territory.def_bonus += improvement.def_bonus
            territory.con_bonus += improvement.con_bonus
            territory.inc_bonus += improvement.inc_bonus
            territory.unr_bonus += improvement.unr_bonus
            # rules flags
            if improvement.name.lower() == 'watchtower': has_watchtower = True
            if improvement.name.lower() == 'fort': has_fort = True
            if improvement.name.lower() == 'road': has_road = True
            if improvement.name.lower() == 'highway': has_highway = True
            if improvement.name.lower() == 'farm': has_farm = True
            if improvement.name.lower() == 'fishery': has_fishery = True
            if improvement.name.lower() in ['mine', 'quarry', 'sawmill']:
                improvements.append(improvement)
        # add bonuses from each feature
        for feature in territory.features.all():
            territory.pop_bonus += feature.pop_bonus
            territory.dan_bonus += feature.dan_bonus
            territory.eco_bonus += feature.eco_bonus
            territory.loy_bonus += feature.loy_bonus
            territory.sta_bonus += feature.sta_bonus
            territory.def_bonus += feature.def_bonus
            territory.con_bonus += feature.con_bonus
            territory.inc_bonus += feature.inc_bonus
            territory.unr_bonus += feature.unr_bonus
            # rules flags
            if feature.name.lower() == 'lair': has_lair = True
            if feature.name.lower() == 'landmark': has_landmark = True
            if feature.name.lower() == 'resource': has_resource = True
        # add bonuses from settlement
        # add rules bonuses
        if has_lair and (has_fort or has_watchtower): territory.def_bonus += 1
        if has_landmark and (has_road or has_highway): territory.loy_bonus += 1
        if len(improvements) > 0:
            for improvement in improvements:
                if improvement.eco_bonus != 0: territory.eco_bonus += 1
                if improvement.loy_bonus != 0: territory.loy_bonus += 1
                if improvement.sta_bonus != 0: territory.sta_bonus += 1
                if improvement.def_bonus != 0: territory.def_bonus += 1
                if improvement.inc_bonus != 0: territory.inc_bonus += 1
        if has_resource and (has_farm or has_fishery): territory.con_bonus -= 1

        # build effects summary
        effects = []
        t = 0
        if territory.pop_bonus != t: effects.append('pop +%s' % territory.pop_bonus)
        if territory.dan_bonus != t: effects.append('danger +%s' % territory.dan_bonus)
        if territory.eco_bonus != t: effects.append('economy +%s' % territory.eco_bonus)
        if territory.loy_bonus != t: effects.append('loyalty +%s' % territory.loy_bonus)
        if territory.sta_bonus != t: effects.append('stability +%s' % territory.sta_bonus)
        if territory.def_bonus != t: effects.append('defense +%s' % territory.def_bonus)
        if territory.con_bonus != t: effects.append('consumption %s' % territory.con_bonus)
        if territory.inc_bonus != t: effects.append('income %s' % territory.inc_bonus)
        if territory.unr_bonus != t: effects.append('unrest %s' % territory.unr_bonus)
        territory.effects_summary = ', '.join(effects)

    return {'territories': territories}
