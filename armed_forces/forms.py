from django import forms
from .models import ArmedForce, Equipment, Casualty


class ArmedForceForm(forms.ModelForm):

    class Meta:
        model = ArmedForce
        fields = (
            'polity', 'name', 'desc', 'commander', 'morale', 'speed', 'active',
            'hit_die', 'type', 'size', 'custom_cr', 'mount_cr', 'equipment', 'special_abilities',
            'tactics_known',
        )


class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = (
            'name', 'desc', 'requirements', 'cost', 'om_mod', 'om_melee_mod', 'om_ranged_mod',
            'dv_mod', 'speed_mod', 'morale_mod'
        )


class CasualtyForm(forms.ModelForm):

    class Meta:
        model = Casualty
        fields = (
            'unit', 'num', 'months'
        )
