from django.db import models

default_max_length = 100


class Type(models.Model):
    name = models.CharField(max_length=default_max_length)
    pop_bonus = models.IntegerField(default=0)
    dan_bonus = models.IntegerField(default=0)
    exp_time = models.IntegerField(default=1)
    prep_time = models.IntegerField(default=1)
    prep_cost = models.IntegerField(default=1)
    farm_cost = models.IntegerField(default=1)
    road_cost = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=default_max_length)
    desc = models.TextField(default="", blank=True, null=True)
    pop_bonus = models.IntegerField(default=0)
    dan_bonus = models.IntegerField(default=0)
    eco_bonus = models.FloatField(default=0)
    loy_bonus = models.FloatField(default=0)
    sta_bonus = models.FloatField(default=0)
    def_bonus = models.IntegerField(default=0)
    con_bonus = models.IntegerField(default=0)
    inc_bonus = models.IntegerField(default=0)
    unr_bonus = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Improvement(models.Model):
    name = models.CharField(max_length=default_max_length)
    pop_bonus = models.IntegerField(default=0)
    dan_bonus = models.IntegerField(default=0)
    eco_bonus = models.FloatField(default=0)
    loy_bonus = models.FloatField(default=0)
    sta_bonus = models.FloatField(default=0)
    fam_bonus = models.IntegerField(default=0)
    inf_bonus = models.IntegerField(default=0)
    def_bonus = models.IntegerField(default=0)
    con_bonus = models.IntegerField(default=0)
    inc_bonus = models.IntegerField(default=0)
    unr_bonus = models.IntegerField(default=0)
    cost_per_month = models.IntegerField(default=0)
    construction_time = models.IntegerField(default=0)
    exclusive = models.BooleanField()
    desc = models.TextField(default="")

    def __str__(self):
        return self.name


class Map(models.Model):
    name = models.CharField(max_length=default_max_length)

    def __str__(self):
        return self.name


class Territory(models.Model):
    polity = models.ForeignKey(
        'polity.Polity', on_delete=models.CASCADE, default=1,
        related_name='territory', related_query_name='territory',
        null=True, blank=True,
    )
    map = models.ForeignKey(
        Map, on_delete=models.CASCADE, default=1,
        related_name='territory', related_query_name='territory'
    )
    hex = models.IntegerField()
    type = models.ForeignKey(
        Type, on_delete=models.CASCADE, default=1,
        related_name='territory', related_query_name='territory'
    )
    features = models.ManyToManyField(
        Feature, related_name='territory', related_query_name='territory',
        blank=True,
    )
    improvements = models.ManyToManyField(
        Improvement, related_name='territory', related_query_name='territory',
        blank=True,
    )
    notes = models.TextField(blank=True, null=True)

    def get_effects_summary(self):
        return self.type.name

    def __str__(self):
        if self.polity is not None:
            name = "%s (%s)" % (self.hex, self.polity.name)
        else:
            name = "%s" % self.hex
        return name
