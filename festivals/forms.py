from django import forms
from .models import Festival


class FestivalForm(forms.ModelForm):

    class Meta:
        model = Festival
        fields = (
            'polity', 'name', 'type', 'target_settlement', 'target_hex', 'success_level'
        )
