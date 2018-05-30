from django.db import models
from common.utils import get_effects_summary

default_max_length = 100


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
        if effects_summary == '': effects_summary = "No Modifiers"
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
        if effects_summary == '': effects_summary = "No Modifiers"
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
        if effects_summary == '': effects_summary = "No Modifiers"
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
    fame = models.IntegerField(default=0)
    infamy = models.IntegerField(default=0)
    desc = models.TextField(default="", blank=True)
    tax_edict = models.ForeignKey(
        'core.TaxEdict', on_delete=models.CASCADE,
        related_name='polity', related_query_name='polity')
    promotion_edict = models.ForeignKey(
        'core.PromotionEdict', on_delete=models.CASCADE,
        related_name='polity', related_query_name='polity')
    holiday_edict = models.ForeignKey(
        'core.HolidayEdict', on_delete=models.CASCADE,
        related_name='polity', related_query_name='polity')
    recruitment_edict = models.ForeignKey(
        'core.RecruitmentEdict', on_delete=models.CASCADE,
        related_name='polity', related_query_name='polity')
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
