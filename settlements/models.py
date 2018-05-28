from django.db import models

default_max_length = 100


class Type(models.Model):
    name = models.CharField(max_length=default_max_length)
    max_lots = models.IntegerField(blank=True, null=True)
    con_bonus = models.FloatField()
    pop_mult = models.FloatField()
    dan_mod = models.IntegerField()
    att_mod = models.IntegerField()
    magic_items = models.CharField(max_length=default_max_length, blank=True, null=True)

    def __str__(self):
        return self.name


class BuildingType(models.Model):
    name = models.CharField(max_length=default_max_length)
    desc = models.TextField(blank=True)
    const_cost = models.IntegerField()
    const_time = models.IntegerField()
    lots = models.IntegerField(default=1)
    pop_bonus = models.IntegerField(default=0)
    required_settlement_type = models.ForeignKey(
        Type, on_delete=models.CASCADE, default=1,
        related_name='building_type', related_query_name='building_type',
        null=True, blank=True,
    )
    special = models.TextField(blank=True)
    eco_bonus = models.IntegerField(default=0)
    loy_bonus = models.IntegerField(default=0)
    sta_bonus = models.IntegerField(default=0)
    fam_bonus = models.IntegerField(default=0)
    inf_bonus = models.FloatField(default=0)
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
    dan_bonus = models.IntegerField(default=0)
    discounts = models.ManyToManyField(
        'self',
        related_name='discounted_from', related_query_name='discounted_from',
        blank=True,
    )
    upgrade_to = models.ManyToManyField(
        'self',
        related_name='upgrade_from', related_query_name='upgrade_from',
        blank=True,
    )
    limit = models.IntegerField(null=True, blank=True)
    magic_items = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name


class Settlement(models.Model):
    territory = models.ForeignKey(
        'territory.Territory', on_delete=models.CASCADE,
        related_name='settlement', related_query_name='settlement'
    )
    name = models.CharField(max_length=default_max_length)
    districts = models.IntegerField(default=0)

    def __str__(self):
        return "%s (%s)" % (self.name, self.territory.polity.name)


class Building(models.Model):
    settlement = models.ForeignKey(
        Settlement, on_delete=models.CASCADE,
        related_name='building', related_query_name='building',
    )
    name = models.CharField(max_length=default_max_length, blank=True, null=True)
    type = models.ForeignKey(
        BuildingType, on_delete=models.CASCADE,
        related_name='building', related_query_name='building',
    )
    lots = models.IntegerField(default=None, null=True, blank=True)

    def __str__(self):
        return self.name
