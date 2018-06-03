from django import forms
from .models import Person, NobleRank, Award, Advisor


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = (
            'polity', 'first_name', 'last_name', 'middle_name', 'gender', 'noble_rank',
            'leadership_role', 'advisor', 'awards', 'hit_dice',
            'str', 'dex', 'con', 'int', 'wis', 'cha',
            'notes', 'boons'
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


class AdvisorForm(forms.ModelForm):

    class Meta:
        model = Advisor
        fields = (
            'name', 'desc', 'leadership_bonus',
            'leadership_bonus_eco', 'leadership_bonus_loy', 'leadership_bonus_sta',
            'other_benefits'
        )
