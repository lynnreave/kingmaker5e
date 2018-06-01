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


def get_signed_number(number):
    if number >= 0:
        s = '+%s' % number
    else:
        s = '-%s' % abs(number)
    return {'s': s}


def get_effects_summary(self):
    effects = []
    t = 0
    try:
        if self.pop_bonus != t: effects.append('pop %s' % get_signed_number(self.pop_bonus)['s'])
    except BaseException:
        pass
    try:
        if self.dan_bonus != t: effects.append('danger %s' % get_signed_number(self.dan_bonus)['s'])
    except BaseException:
        pass
    if self.eco_bonus != t: effects.append('economy %s' % get_signed_number(self.eco_bonus)['s'])
    if self.loy_bonus != t: effects.append('loyalty %s' % get_signed_number(self.loy_bonus)['s'])
    if self.sta_bonus != t: effects.append('stability %s' % get_signed_number(self.sta_bonus)['s'])
    if self.fam_bonus != t: effects.append('fame %s' % get_signed_number(self.fam_bonus)['s'])
    if self.inf_bonus != t: effects.append('infamy %s' % get_signed_number(self.inf_bonus)['s'])
    if self.cor_bonus != t: effects.append('corruption %s' % get_signed_number(self.cor_bonus)['s'])
    if self.cri_bonus != t: effects.append('crime %s' % get_signed_number(self.cri_bonus)['s'])
    if self.law_bonus != t: effects.append('law %s' % get_signed_number(self.law_bonus)['s'])
    if self.lor_bonus != t: effects.append('lore %s' % get_signed_number(self.lor_bonus)['s'])
    if self.pro_bonus != t: effects.append('productivity %s' % get_signed_number(self.pro_bonus)['s'])
    if self.soc_bonus != t: effects.append('society %s' % get_signed_number(self.soc_bonus)['s'])
    try:
        if self.def_bonus != t: effects.append('defense %s' % get_signed_number(self.def_bonus)['s'])
    except BaseException:
        pass
    try:
        if self.con_bonus != t: effects.append('consumption %s' % get_signed_number(self.con_bonus)['s'])
    except BaseException:
        pass
    try:
        if self.inc_bonus != t: effects.append('income %s' % get_signed_number(self.inc_bonus)['s'])
    except BaseException:
        pass
    try:
        if self.unr_bonus != t:
            effects.append('unrest %s (permanent)' % get_signed_number(self.unr_bonus)['s'])
    except BaseException:
        pass
    return ', '.join(effects)


def get_effects_summary_for_obj(obj):
    effects = []
    t = 0
    if obj.population != t: effects.append('pop %s' % get_signed_number(obj.population)['s'])
    if obj.danger != t: effects.append('danger %s' % get_signed_number(obj.danger)['s'])
    if obj.economy != t: effects.append('economy %s' % get_signed_number(obj.economy)['s'])
    if obj.loyalty != t: effects.append('loyalty %s' % get_signed_number(obj.loyalty)['s'])
    if obj.stability != t: effects.append('stability %s' % get_signed_number(obj.stability)['s'])
    if obj.fame != t: effects.append('fame %s' % get_signed_number(obj.fame)['s'])
    if obj.infamy != t: effects.append('infamy %s' % get_signed_number(obj.infamy)['s'])
    if obj.corruption != t: effects.append('corruption %s' % get_signed_number(obj.corruption)['s'])
    if obj.crime != t: effects.append('crime %s' % get_signed_number(obj.crime)['s'])
    if obj.law != t: effects.append('law %s' % get_signed_number(obj.law)['s'])
    if obj.lore != t: effects.append('lore %s' % get_signed_number(obj.lore)['s'])
    if obj.productivity != t: effects.append('productivity %s' % get_signed_number(obj.productivity)['s'])
    if obj.society != t: effects.append('society %s' % get_signed_number(obj.society)['s'])
    if obj.defense != t: effects.append('defense %s' % get_signed_number(obj.defense)['s'])
    if obj.consumption != t: effects.append('consumption %s' % get_signed_number(obj.consumption)['s'])
    if obj.income != t: effects.append('income %s' % get_signed_number(obj.income)['s'])
    if obj.unrest != t: effects.append('unrest %s (permanent)' % get_signed_number(obj.unrest)['s'])
    return ', '.join(effects)


def get_mixed_number_string(num):
    if num == 0:
        s = '0'
    elif num < 1:
        s = '%s/%s' % float(num).as_integer_ratio()
    else:
        s = '%s' % int(num)

    return s
