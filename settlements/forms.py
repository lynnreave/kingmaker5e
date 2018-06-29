from django import forms
from .models import Settlement, Building, Stronghold, Expansion, District, Lot


class SettlementForm(forms.ModelForm):

    class Meta:
        model = Settlement
        fields = (
            'name', 'territory', 'capital'
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
            'type', 'custom_name', 'custom_slots', 'custom_income', 'desc', 'features',
        )


class DistrictForm(forms.ModelForm):

    class Meta:
        model = District
        fields = (
            'name',
        )


class LotForm(forms.ModelForm):

    class Meta:
        model = Lot
        fields = (
            'building', 'img', 'notes',
        )
