from django.db import models
from common.utils import get_effects_summary

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


class Deity(models.Model):
    name = models.CharField(max_length=default_max_length)

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
        Type, on_delete=models.SET_NULL, default=1,
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

    def get_effects_summary(self):
        effects_summary = get_effects_summary(self)
        if self.magic_items != '' and self.magic_items is not None:
            effects_summary += ', %s' % self.magic_items
        if self.name.lower() in ['shrine', 'temple', 'cathedral']:
            effects_summary += ', + additional bonuses based on deity'
        return effects_summary

    def __str__(self):
        self.get_effects_summary()
        return "%s (%s)" % (self.name, self.get_effects_summary())


class BuildingEnhancement(models.Model):
    name = models.CharField(max_length=default_max_length)
    desc = models.TextField(blank=True)
    cost = models.IntegerField(default=0)
    cost_per_lot = models.BooleanField(default=False)
    pop_bonus = models.IntegerField(default=0)
    dan_bonus = models.IntegerField(default=0)
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
        return "%s (%s)" % (self.name, get_effects_summary(self))


class Settlement(models.Model):
    territory = models.ForeignKey(
        'territory.Territory', on_delete=models.SET_NULL,
        related_name='settlement', related_query_name='settlement',
        null=True, blank=True
    )
    name = models.CharField(max_length=default_max_length)
    capital = models.BooleanField(default=False)

    def __str__(self):
        if self.territory.polity is not None:
            name = "%s (%s)" % (self.name, self.territory.polity.name)
        else:
            name = self.name
        return name


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
    enhancements = models.ManyToManyField(
        BuildingEnhancement, related_name='building', related_query_name='building', blank=True,
    )
    deity = models.ForeignKey(
        Deity, on_delete=models.SET_NULL,
        related_name='building', related_query_name='building',
        null=True, blank=True,
    )
    endowment = models.BooleanField(default=False)
    free_endowment = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class StrongholdType(models.Model):
    name = models.CharField(max_length=default_max_length)
    desc = models.TextField(blank=True)
    expansion_slots = models.IntegerField(default=1)
    cost = models.IntegerField(default=5000)
    construction_time = models.IntegerField(default=1)
    upkeep = models.IntegerField(default=0)
    hirelings_skilled = models.IntegerField(default=0)
    hirelings_unskilled = models.IntegerField(default=0)

    def __str__(self):
        return "%s (%s gp, %s gp)" % (self.name, self.cost, self.upkeep)


class Stronghold(models.Model):
    polity = models.ForeignKey(
        'polity.Polity', on_delete=models.CASCADE, default=1,
        related_name='stronghold', related_query_name='stronghold',
    )
    custom_name = models.CharField(max_length=default_max_length, null=True, blank=True)
    type = models.ForeignKey(
        StrongholdType, on_delete=models.CASCADE,
        related_name='stronghold', related_query_name='stronghold',
    )
    building = models.ForeignKey(
        Building, on_delete=models.SET_NULL,
        related_name='stronghold', related_query_name='stronghold',
        null=True, blank=True,
    )
    territory = models.ForeignKey(
        'territory.Territory', on_delete=models.SET_NULL,
        related_name='stronghold', related_query_name='stronghold',
        null=True, blank=True,
    )

    def __str__(self):
        if self.custom_name is not None:
            name = self.custom_name
        elif self.building is not None:
            name = self.building.name
        else:
            name = "Unnamed"
        return name


class ExpansionType(models.Model):
    name = models.CharField(max_length=default_max_length)
    desc = models.TextField(blank=True)
    slots = models.IntegerField(default=1)
    cost = models.IntegerField()
    construction_time = models.IntegerField(default=1)
    benefit = models.TextField(blank=True)
    income = models.CharField(max_length=default_max_length, blank=True, null=True)

    def __str__(self):
        return "%s (%s)" % (self.name, self.slots)


class ExpansionFeature(models.Model):
    name = models.CharField(max_length=default_max_length)
    desc = models.TextField(blank=True)
    reqs = models.TextField(blank=True)
    cost = models.IntegerField()
    construction_time = models.IntegerField(default=1)
    benefit = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Expansion(models.Model):
    stronghold = models.ForeignKey(
        Stronghold, on_delete=models.CASCADE,
        related_name='expansion', related_query_name='expansion',
    )
    type = models.ForeignKey(
        ExpansionType, on_delete=models.CASCADE,
        related_name='expansion', related_query_name='expansion',
    )
    features = models.ManyToManyField(
        ExpansionFeature,
        related_name='expansion', related_query_name='expansion',
        blank=True,
    )
    custom_name = models.CharField(max_length=default_max_length, null=True, blank=True)
    custom_slots = models.IntegerField(null=True, blank=True)
    custom_income = models.CharField(max_length=default_max_length, null=True, blank=True)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.type.name


class District(models.Model):
    settlement = models.ForeignKey(
        Settlement, on_delete=models.CASCADE,
        related_name='district', related_query_name='district',
    )
    name = models.CharField(max_length=default_max_length)

    def __str__(self):
        return self.name


class Lot(models.Model):
    district = models.ForeignKey(
        District, on_delete=models.CASCADE,
        related_name='lot', related_query_name='lot',
    )
    grid = models.IntegerField()
    building = models.ForeignKey(
        Building, on_delete=models.SET_NULL,
        related_name='lot', related_query_name='lot',
        null=True, blank=True,
    )
    img = models.CharField(max_length=default_max_length, null=True, blank=True)

    def __str__(self):
        return self.grid
