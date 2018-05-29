from django import forms
from .models import Army


class ArmyForm(forms.ModelForm):

    class Meta:
        model = Army
        fields = (
            'polity', 'name',
        )
