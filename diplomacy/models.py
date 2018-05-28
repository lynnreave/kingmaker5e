from django.db import models

default_max_length = 100


class Attitude(models.Model):
    step = models.IntegerField(unique=True)
    name = models.CharField(max_length=default_max_length)

    def __str__(self):
        return self.name


class Treaty(models.Model):
    name = models.CharField(max_length=default_max_length)
    eco_mult = models.FloatField(default=0)
    sta_mult = models.FloatField(default=0)

    def __str__(self):
        return self.name


class DiplomaticRelation(models.Model):
    holder = models.ForeignKey(
        'polity.Polity', on_delete=models.CASCADE, default=1,
        related_name='diplomatic_relation', related_query_name='diplomatic_relation'
    )
    target = models.CharField(max_length=default_max_length, unique=True)
    attitude = models.ForeignKey(
        Attitude, on_delete=models.CASCADE,
        related_name='DiplomaticRelation', related_query_name='DiplomaticRelation',
        null=True, blank=True,
    )
    treaties = models.ManyToManyField(
        Treaty, related_name='diplomatic_relation', related_query_name='diplomatic_relation',
        blank=True,
    )
    size = models.IntegerField(null=True, blank=True)
    economy = models.IntegerField(null=True, blank=True)
    stability = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "%s:%s" % (self.holder, self.target)
