from django import forms
from .models import Territory, Type, Feature, Improvement


class TerritoryForm(forms.ModelForm):

    class Meta:
        model = Territory
        fields = (
            'hex', 'polity', 'type', 'features', 'improvements',
        )


class TypeForm(forms.ModelForm):

    class Meta:
        model = Type
        fields = (
            'name', 'pop_bonus', 'dan_bonus', 'exp_time', 'prep_time', 'prep_cost',
            'farm_cost', 'road_cost',
        )


class FeatureForm(forms.ModelForm):

    class Meta:
        model = Feature
        fields = (
            'name', 'desc', 'pop_bonus', 'dan_bonus',
            'eco_bonus', 'loy_bonus', 'sta_bonus', 'def_bonus',
            'con_bonus', 'inc_bonus', 'unr_bonus',
        )


class ImprovementForm(forms.ModelForm):

    class Meta:
        model = Improvement
        fields = (
            'name', 'pop_bonus', 'eco_bonus', 'loy_bonus', 'sta_bonus', 'def_bonus',
            'con_bonus', 'inc_bonus', 'unr_bonus', 'cost_per_month', 'construction_time',
            'exclusive', 'desc',
        )
