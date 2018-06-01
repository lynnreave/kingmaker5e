from django import forms
from .models import Settlement, Building, Stronghold, Expansion


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
            'name', 'type', 'lots', 'enhancements', 'deity', 'endowment', 'free_endowment'
        )


class StrongholdForm(forms.ModelForm):

    class Meta:
        model = Stronghold
        fields = (
            'polity', 'custom_name', 'type', 'building', 'territory'
        )


class ExpansionForm(forms.ModelForm):

    class Meta:
        model = Expansion
        fields = (
            'type', 'custom_name', 'custom_slots', 'desc', 'features',
        )
