from django.db import models

default_max_length = 100


class Award(models.Model):
    name = models.CharField(max_length=default_max_length)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=default_max_length)

    def __str__(self):
        return self.name


class NobleRank(models.Model):
    rank = models.CharField(max_length=default_max_length)
    male_title = models.CharField(max_length=default_max_length)
    female_title = models.CharField(max_length=default_max_length)
    male_honorific = models.CharField(max_length=default_max_length)
    female_honorific = models.CharField(max_length=default_max_length)
    desc = models.TextField(blank=True)

    def __str__(self):
        return "%s/%s (%s)" % (self.male_title, self.female_title, self.rank)


class LeadershipRole(models.Model):
    name = models.CharField(max_length=default_max_length)
    ranking = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Advisor(models.Model):
    name = models.CharField(max_length=default_max_length)
    desc = models.TextField(default="", blank=True)
    leadership_bonus = models.IntegerField(default=0)
    leadership_bonus_eco = models.IntegerField(default=0)
    leadership_bonus_loy = models.IntegerField(default=0)
    leadership_bonus_sta = models.IntegerField(default=0)
    other_benefits = models.TextField(default="", blank=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=default_max_length)
    middle_name = models.CharField(max_length=default_max_length, blank=True)
    last_name = models.CharField(max_length=default_max_length, blank=True)
    gender = models.ForeignKey(
        Gender, on_delete=models.SET_NULL, related_name='person', related_query_name='person',
        blank=True, null=True,
    )
    noble_rank = models.ForeignKey(
        NobleRank, on_delete=models.SET_NULL, related_name='person', related_query_name='person',
        blank=True, null=True
    )
    awards = models.ManyToManyField(
        Award, blank=True,
        related_name='person', related_query_name='person',
    )
    hit_dice = models.IntegerField(default=1)
    str = models.IntegerField(default=10)
    dex = models.IntegerField(default=10)
    con = models.IntegerField(default=10)
    int = models.IntegerField(default=10)
    wis = models.IntegerField(default=10)
    cha = models.IntegerField(default=10)
    notes = models.TextField(blank=True)
    polity = models.ForeignKey(
        'polity.Polity', on_delete=models.SET_NULL,
        related_name='person', related_query_name='person',
        null=True, blank=True
    )
    advisor = models.ForeignKey(
        Advisor, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='person', related_query_name='person'
    )
    leadership_role = models.ForeignKey(
        LeadershipRole, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='person', related_query_name='person'
    )
    boons = models.ManyToManyField(
        'armed_forces.Boon', blank=True,
        related_name='person', related_query_name='person',
    )

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
