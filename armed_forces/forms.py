from django import forms
from .models import ArmedForce


class ArmedForceForm(forms.ModelForm):

    class Meta:
        model = ArmedForce
        fields = (
            'polity', 'name', 'desc', 'commander', 'morale', 'speed',
            'hit_die', 'type', 'size', 'custom_cr'
        )
