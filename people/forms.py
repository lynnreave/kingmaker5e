from django import forms
from .models import Person


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = (
            'first_name', 'last_name', 'middle_name', 'gender', 'noble_rank',
            'str', 'dex', 'con', 'int', 'wis', 'cha',
            'notes',
        )