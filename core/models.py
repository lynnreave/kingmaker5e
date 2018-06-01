from django.db import models
from common import get_signed_number

default_max_length = 100


class HolidayEdict(models.Model):
    frequency = models.CharField(max_length=default_max_length)
    eco_bonus = models.IntegerField()
    loy_bonus = models.IntegerField()
    con_bonus = models.IntegerField()
    con_dice = models.IntegerField(null=True, blank=True)

    def __str__(self):
        if self.con_dice is not None:
            consumption = 'd'.join([get_signed_number(self.con_bonus)['s'], str(self.con_dice)])
        else:
            consumption = get_signed_number(self.con_bonus)['s']
        return "%s (%s Economy, %s Loyalty, %s Consumption)" % (
            self.frequency,
            get_signed_number(self.eco_bonus)['s'],
            get_signed_number(self.loy_bonus)['s'],
            consumption
        )


class PromotionEdict(models.Model):
    attitude = models.CharField(max_length=default_max_length)
    hex_claims = models.IntegerField()
    eco_bonus = models.IntegerField()
    loy_bonus = models.IntegerField()
    sta_bonus = models.IntegerField()
    con_bonus = models.IntegerField()
    con_dice = models.IntegerField(null=True, blank=True)

    def __str__(self):
        if self.con_dice is not None:
            consumption = 'd'.join([get_signed_number(self.con_bonus)['s'], str(self.con_dice)])
        else:
            consumption = get_signed_number(self.con_bonus)['s']
        return "%s (%s Hex Claims, %s Economy, %s Loyalty, %s Stability, %s Consumption)" % (
            self.attitude, get_signed_number(self.hex_claims)['s'],
            get_signed_number(self.eco_bonus)['s'],
            get_signed_number(self.loy_bonus)['s'],
            get_signed_number(self.sta_bonus)['s'],
            consumption
        )


class RecruitmentEdict(models.Model):
    militarism = models.CharField(max_length=default_max_length)
    manpower_mult = models.FloatField()
    elites_mult = models.FloatField()
    fam_bonus = models.IntegerField()
    inf_bonus = models.IntegerField()
    def_bonus = models.IntegerField()
    eco_bonus = models.IntegerField()
    soc_bonus = models.IntegerField()

    def __str__(self):
        return "%s (%s Manpower, %s Elites, %s Fame, %s Infamy, " \
               "%s Defense, %s Economy, %s Society)" % (
                self.militarism, self.manpower_mult, self.elites_mult,
                get_signed_number(self.fam_bonus)['s'],
                get_signed_number(self.inf_bonus)['s'],
                get_signed_number(self.def_bonus)['s'],
                get_signed_number(self.eco_bonus)['s'],
                get_signed_number(self.soc_bonus)['s'],
        )


class TaxEdict(models.Model):
    tax_level = models.CharField(max_length=default_max_length)
    revenue_divisor = models.FloatField()
    eco_bonus = models.IntegerField()
    loy_bonus = models.IntegerField()

    def __str__(self):
        return "%s (%s Economy, %s Loyalty, Revenue/%s)" % (
            self.tax_level, get_signed_number(self.eco_bonus)['s'],
            get_signed_number(self.loy_bonus)['s'],
            self.revenue_divisor
        )


class Month(models.Model):
    name = models.CharField(max_length=default_max_length)
    equivalent = models.CharField(max_length=default_max_length)

    def __str__(self):
        return "%s (%s)" % (self.name, self.equivalent)
