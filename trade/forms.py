from django import forms
from .models import TradeRoute


class TradeRouteForm(forms.ModelForm):

    class Meta:
        model = TradeRoute
        fields = (
            'polity', 'settlement', 'target', 'type', 'success_level', 'length', 'investment',
            'active'
        )
