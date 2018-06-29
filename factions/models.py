from django.db import models

default_max_length = 100


class Type(models.Model):
    name = models.CharField(max_length=default_max_length)

    def __str__(self):
        return self.name


class Faction(models.Model):
    polity = models.ForeignKey(
        'polity.Polity', on_delete=models.CASCADE,
        related_name='faction', related_query_name='faction'
    )
    name = models.CharField(max_length=default_max_length)
    type = models.ForeignKey(
        Type, on_delete=models.SET_NULL,
        related_name='faction', related_query_name='faction',
        null=True, blank=True,
    )
    size = models.IntegerField(default=1)
    desc = models.TextField(blank=True)
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
        return self.name
