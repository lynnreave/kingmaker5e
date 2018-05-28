from django.db import models

from django.db import models

default_max_length = 100


class Event(models.Model):
    name = models.CharField(max_length=default_max_length)
    desc = models.TextField(blank=True)
    polity = models.ForeignKey(
        'polity.Polity', on_delete=models.CASCADE,
        related_name='event', related_query_name='event'
    )
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
    def_bonus = models.IntegerField(default=0)
    con_bonus = models.IntegerField(default=0)
    inc_bonus = models.IntegerField(default=0)
    unr_bonus = models.IntegerField(default=0)

    def __str__(self):
        return self.name
