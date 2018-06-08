from django.db import models

default_max_length = 100


class RouteType(models.Model):
    name = models.CharField(max_length=default_max_length)

    def __str__(self):
        return self.name


class SuccessLevel(models.Model):
    name = models.CharField(max_length=default_max_length)
    fam_bonus = models.IntegerField(default=0)
    eco_bonus = models.IntegerField(default=0)
    fame_increment = models.IntegerField(default=0)
    unrest_increment = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class TradeRoute(models.Model):
    polity = models.ForeignKey(
        'polity.Polity', on_delete=models.CASCADE,
        related_name='trade_route', related_query_name='trade_route'
    )
    settlement = models.ForeignKey(
        'settlements.Settlement', on_delete=models.CASCADE,
        related_name='trade_route', related_query_name='trade_route'
    )
    target = models.CharField(max_length=default_max_length)
    type = models.ForeignKey(
        RouteType, on_delete=models.CASCADE,
        related_name='trade_route', related_query_name='trade_route'
    )
    success_level = models.ForeignKey(
        SuccessLevel, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='trade_route', related_query_name='trade_route'
    )
    length = models.IntegerField(default=1)
    investment = models.IntegerField(default=5)
    active = models.BooleanField(default=False)

    def get_description(self):
        return "%s to %s (%s)" % (self.settlement.name, self.target, self.type.name)

    def __str__(self):
        return self.get_description()
