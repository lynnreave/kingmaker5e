from django.db import models

default_max_length = 100


def get_effects_summary(self):
    effects = []
    if self.eco_bonus > 0: effects.append('+%d Economy' % self.eco_bonus)
    elif self.eco_bonus < 0: effects.append('-%d Economy' % self.eco_bonus)
    if self.loy_bonus > 0: effects.append('+%d Loyalty' % self.loy_bonus)
    elif self.loy_bonus < 0: effects.append('-%d Loyalty' % self.loy_bonus)
    if self.sta_bonus > 0: effects.append('+%d Stability' % self.sta_bonus)
    elif self.sta_bonus < 0: effects.append('-%d Stability' % self.sta_bonus)
    if self.fam_bonus > 0: effects.append('+%d Fame' % self.fam_bonus)
    elif self.fam_bonus < 0: effects.append('-%d Fame' % self.fam_bonus)
    if self.inf_bonus > 0: effects.append('+%d Infamy' % self.inf_bonus)
    elif self.inf_bonus < 0: effects.append('-%d Infamy' % self.inf_bonus)
    if self.cor_bonus > 0: effects.append('+%d Corruption' % self.cor_bonus)
    elif self.cor_bonus < 0: effects.append('-%d Corruption' % self.cor_bonus)
    if self.cri_bonus > 0: effects.append('+%d Crime' % self.cri_bonus)
    elif self.cri_bonus < 0: effects.append('-%d Crime' % self.cri_bonus)
    if self.law_bonus > 0: effects.append('+%d Law' % self.law_bonus)
    elif self.law_bonus < 0: effects.append('-%d Law' % self.law_bonus)
    if self.lor_bonus > 0: effects.append('+%d Lore' % self.lor_bonus)
    elif self.lor_bonus < 0: effects.append('-%d Lore' % self.lor_bonus)
    if self.pro_bonus > 0: effects.append('+%d Productivity' % self.pro_bonus)
    elif self.pro_bonus < 0: effects.append('-%d Productivity' % self.pro_bonus)
    if self.soc_bonus > 0: effects.append('+%d Society' % self.soc_bonus)
    elif self.soc_bonus < 0: effects.append('-%d Society' % self.soc_bonus)
    if len(effects) > 0: effects_summary = ", ".join(effects)
    else: effects_summary = "No Modifiers"
    return effects_summary


class AlignmentLC(models.Model):
    name = models.CharField(max_length=default_max_length)
    eco_bonus = models.IntegerField(default=0)
    loy_bonus = models.IntegerField(default=0)
    sta_bonus = models.IntegerField(default=0)
    fam_bonus = models.IntegerField(default=0)
    inf_bonus = models.IntegerField(default=0)
    cor_bonus = models.IntegerField(default=0)
    cri_bonus = models.IntegerField(default=0)
    law_bonus = models.IntegerField(default=0)
    lor_bonus = models.IntegerField(default=0)
    pro_bonus = models.IntegerField(default=0)
    soc_bonus = models.IntegerField(default=0)

    def __str__(self):
        effects_summary = get_effects_summary(self)
        return "%s (%s)" % (self.name, effects_summary)


class AlignmentGE(models.Model):
    name = models.CharField(max_length=default_max_length)
    eco_bonus = models.IntegerField(default=0)
    loy_bonus = models.IntegerField(default=0)
    sta_bonus = models.IntegerField(default=0)
    fam_bonus = models.IntegerField(default=0)
    inf_bonus = models.IntegerField(default=0)
    cor_bonus = models.IntegerField(default=0)
    cri_bonus = models.IntegerField(default=0)
    law_bonus = models.IntegerField(default=0)
    lor_bonus = models.IntegerField(default=0)
    pro_bonus = models.IntegerField(default=0)
    soc_bonus = models.IntegerField(default=0)

    def __str__(self):
        effects_summary = get_effects_summary(self)
        return "%s (%s)" % (self.name, effects_summary)


class Government(models.Model):
    name = models.CharField(max_length=default_max_length)
    desc = models.TextField(default="", blank=True)
    eco_bonus = models.IntegerField(default=0)
    loy_bonus = models.IntegerField(default=0)
    sta_bonus = models.IntegerField(default=0)
    fam_bonus = models.IntegerField(default=0)
    inf_bonus = models.IntegerField(default=0)
    cor_bonus = models.IntegerField(default=0)
    cri_bonus = models.IntegerField(default=0)
    law_bonus = models.IntegerField(default=0)
    lor_bonus = models.IntegerField(default=0)
    pro_bonus = models.IntegerField(default=0)
    soc_bonus = models.IntegerField(default=0)

    def __str__(self):
        effects_summary = get_effects_summary(self)
        return "%s (%s)" % (self.name, effects_summary)


class Attribute(models.Model):
    name = models.CharField(max_length=default_max_length)

    def __str__(self):
        return self.name


class Polity(models.Model):
    name = models.CharField(max_length=default_max_length)
    government = models.ForeignKey(
        Government, on_delete=models.CASCADE,
        related_name='polity', related_query_name='polity')
    alignment_lc = models.ForeignKey(
        AlignmentLC, on_delete=models.CASCADE,
        related_name='polity', related_query_name='polity')
    alignment_ge = models.ForeignKey(
        AlignmentGE, on_delete=models.CASCADE,
        related_name='polity', related_query_name='polity')
    treasury = models.IntegerField(default=0)
    unrest = models.IntegerField(default=0)
    desc = models.TextField(default="", blank=True)
    ruler_attribute_1 = models.ForeignKey(
        Attribute, on_delete=models.CASCADE, null=True, blank=True,
        related_name='polity_ruler_1', related_query_name='polity_ruler_1')
    ruler_attribute_2 = models.ForeignKey(
        Attribute, on_delete=models.CASCADE, null=True, blank=True,
        related_name='polity_ruler_2', related_query_name='polity_ruler_2')
    ruler_attribute_3 = models.ForeignKey(
        Attribute, on_delete=models.CASCADE, null=True, blank=True,
        related_name='polity_ruler_3', related_query_name='polity_ruler_3')
    spymaster_attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE, null=True, blank=True,
        related_name='polity_spymaster', related_query_name='polity_spymaster')

    def __str__(self):
        return self.name
