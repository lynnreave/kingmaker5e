from django import forms
from .models import Settlement, Building


class SettlementForm(forms.ModelForm):

    class Meta:
        model = Settlement
        fields = (
            'name', 'territory', 'districts', 'capital'
        )


class BuildingForm(forms.ModelForm):

    class Meta:
        model = Building
        fields = (
            'name', 'type', 'lots', 'enhancements', 'endowment', 'free_endowment'
        )
