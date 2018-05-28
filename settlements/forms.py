from django import forms
from .models import Settlement


class SettlementForm(forms.ModelForm):

    class Meta:
        model = Settlement
        fields = (
            'name', 'territory',
        )
