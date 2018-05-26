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
    desc = models.TextField(default="")

    def __str__(self):
        return self.name


class Improvement(models.Model):
    name = models.CharField(max_length=default_max_length)
    pop_bonus = models.IntegerField(default=0)
    eco_bonus = models.FloatField(default=0)
    loy_bonus = models.FloatField(default=0)
    sta_bonus = models.FloatField(default=0)
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


class Territory(models.Model):
    hex = models.CharField(max_length=20, null=True)
    type = models.ForeignKey(
        Type, on_delete=models.CASCADE,
        related_name='territory', related_query_name='territories'
    )
    features = models.ManyToManyField(
        Feature, related_name='territory', related_query_name='territories',
        blank=True,
    )
    improvements = models.ManyToManyField(
        Improvement, related_name='territory', related_query_name='territories',
        blank=True,
    )

    def __str__(self):
        return "%s (%s)" % (self.type, self.pk)
