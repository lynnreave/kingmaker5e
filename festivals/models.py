from django.db import models

default_max_length = 100
CIVIC_BUILDINGS = [
    'arena', 'black market', 'bordello', 'dance hall', 'gambling den', 'inn', 'luxury shop',
    'market', 'monument', 'palace', 'park', 'shop', 'tavern'
]
RELIGIOUS_BUILDINGS = [
    'cathedral', 'graveyard', 'inn', 'luxury shop', 'market', 'monument', 'park', 'shop', 'shrine',
    'temple'
]


class Type(models.Model):
    name = models.CharField(max_length=default_max_length)
    desc = models.TextField(blank=True)
    law_bonus = models.IntegerField(default=0)
    cri_bonus = models.IntegerField(default=0)
    soc_bonus = models.IntegerField(default=0)
    sta_bonus = models.IntegerField(default=0)

    def __str__(self):
        return "%s (%s)" % (self.name, self.desc)


class SuccessLevel(models.Model):
    name = models.CharField(max_length=default_max_length)
    effect_mult = models.FloatField(default=1.0)

    def __str__(self):
        return self.name


class Festival(models.Model):
    polity = models.ForeignKey(
        'polity.Polity', on_delete=models.CASCADE,
        related_name='festival', related_query_name='festival'
    )
    name = models.CharField(max_length=default_max_length)
    type = models.ForeignKey(
        Type, on_delete=models.CASCADE,
        related_name='festival', related_query_name='festival'
    )
    desc = models.TextField(blank=True)
    target_settlement = models.ForeignKey(
        'settlements.Settlement', on_delete=models.CASCADE, null=True, blank=True,
        related_name='festival', related_query_name='festival'
    )
    target_hex = models.ForeignKey(
        'territory.Territory', on_delete=models.CASCADE, null=True, blank=True,
        related_name='festival', related_query_name='festival'
    )
    success_level = models.ForeignKey(
        SuccessLevel, on_delete=models.CASCADE,
        related_name='festival', related_query_name='festival'
    )

    def __str__(self):
        return self.name
