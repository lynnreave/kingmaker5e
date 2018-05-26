from django import forms
from .models import Polity


class PolityForm(forms.ModelForm):

    class Meta:
        model = Polity
        fields = ('name', 'desc', )
