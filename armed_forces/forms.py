from django import forms
from .models import ArmedForce, Equipment


class ArmedForceForm(forms.ModelForm):

    class Meta:
        model = ArmedForce
        fields = (
            'polity', 'name', 'desc', 'commander', 'morale', 'speed', 'active',
            'hit_die', 'type', 'size', 'custom_cr', 'equipment'
        )


class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = (
            'name', 'desc', 'requirements', 'cost', 'om_mod', 'om_melee_mod', 'om_ranged_mod',
            'dv_mod', 'speed_mod', 'morale_mod',
        )
