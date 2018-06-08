from django.db import models

default_max_length = 100


class SoldierType(models.Model):
    name = models.CharField(max_length=default_max_length)
    default_cr = models.FloatField(default=1)

    def __str__(self):
        return self.name


class UnitType(models.Model):
    name = models.CharField(max_length=default_max_length)
    num_soldiers = models.IntegerField(default=1)
    acr_mod = models.IntegerField(default=0)
    equip_cost_mult = models.FloatField(default=1)
    camo_mod = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=default_max_length)
    desc = models.TextField(blank=True)
    requirements = models.ManyToManyField(
        'settlements.BuildingType',
        related_name='required_for_equipment', related_query_name='required_for_equipment',
        blank=True,
    )
    cost = models.IntegerField()
    om_mod = models.IntegerField(default=0)
    om_melee_mod = models.IntegerField(default=0)
    om_ranged_mod = models.IntegerField(default=0)
    dv_mod = models.IntegerField(default=0)
    speed_mod = models.IntegerField(default=0)
    morale_mod = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Boon(models.Model):
    name = models.CharField(max_length=default_max_length)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name


class SpecialAbility(models.Model):
    name = models.CharField(max_length=default_max_length)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Tactic(models.Model):
    name = models.CharField(max_length=default_max_length)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ArmedForce(models.Model):
    polity = models.ForeignKey(
        'polity.Polity', on_delete=models.SET_NULL,
        related_name='armed_force', related_query_name='armed_force',
        null=True, blank=True
    )
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=default_max_length)
    desc = models.TextField(blank=True, default='')
    morale = models.IntegerField(default=0)
    speed = models.IntegerField(default=1)
    hit_die = models.IntegerField(default=10)
    type = models.ForeignKey(
        SoldierType, on_delete=models.SET_NULL, default=1,
        related_name='armed_force', related_query_name='armed_force',
        null=True, blank=True
    )
    size = models.ForeignKey(
        UnitType, on_delete=models.SET_NULL, default=1, null=True, blank=True,
        related_name='armed_force', related_query_name='armed_force',
    )
    commander = models.ForeignKey(
        'people.Person', on_delete=models.SET_NULL, default=None, null=True, blank=True,
        related_name='armed_force', related_query_name='armed_force',
    )
    equipment = models.ManyToManyField(
        Equipment, related_name='armed_force', related_query_name='armed_force', blank=True,
    )
    special_abilities = models.ManyToManyField(
        SpecialAbility, related_name='armed_force', related_query_name='armed_force', blank=True,
    )
    tactics_known = models.ManyToManyField(
        Tactic, related_name='armed_force', related_query_name='armed_force', blank=True, default=20,
    )
    custom_cr = models.FloatField(null=True, blank=True)
    mount_cr = models.FloatField(null=True, blank=True)

    def __str__(self):
        return "%s (%s)" % (self.name, self.polity.name)


class Casualty(models.Model):
    unit = models.ForeignKey(
        ArmedForce, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='casualty', related_query_name='casualty'
    )
    num = models.IntegerField()
    months = models.IntegerField()

    def __str__(self):
        if self.unit is not None:
            name = "%s from %s" % (self.num, self.unit.name)
        else:
            name = self.num
        return name
