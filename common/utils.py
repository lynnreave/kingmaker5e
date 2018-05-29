def get_signed_number(number):
    if number >= 0:
        s = '+%s' % number
    else:
        s = '-%s' % abs(number)
    return {'s': s}


def get_effects_summary(self):
    effects = []
    t = 0
    if self.pop_bonus != t: effects.append('pop %s' % get_signed_number(self.pop_bonus)['s'])
    if self.dan_bonus != t: effects.append('danger %s' % get_signed_number(self.dan_bonus)['s'])
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
    if self.def_bonus != t: effects.append('defense %s' % get_signed_number(self.def_bonus)['s'])
    if self.con_bonus != t: effects.append('consumption %s' % get_signed_number(self.con_bonus)['s'])
    if self.inc_bonus != t: effects.append('income %s' % get_signed_number(self.inc_bonus)['s'])
    if self.unr_bonus != t: effects.append('unrest %s' % get_signed_number(self.unr_bonus)['s'])
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
    if obj.unrest != t: effects.append('unrest %s' % get_signed_number(obj.unrest)['s'])
    return ', '.join(effects)
