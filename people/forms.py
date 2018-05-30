from django import forms
from .models import Person, NobleRank, Award


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = (
            'first_name', 'last_name', 'middle_name', 'gender', 'noble_rank', 'leadership_role',
            'awards', 'hit_dice',
            'str', 'dex', 'con', 'int', 'wis', 'cha',
            'notes', 'polity',
        )


class NobleRankForm(forms.ModelForm):

    class Meta:
        model = NobleRank
        fields = (
            'rank', 'male_title', 'female_title', 'male_honorific', 'female_honorific', 'desc',
        )


class AwardForm(forms.ModelForm):

    class Meta:
        model = Award
        fields = (
            'name', 'desc',
        )
