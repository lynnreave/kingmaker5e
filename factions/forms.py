from django import forms
from .models import Faction


class FactionForm(forms.ModelForm):

    class Meta:
        model = Faction
        fields = (
            'polity', 'name', 'type', 'desc', 'eco_bonus', 'sta_bonus', 'loy_bonus',
            'fam_bonus', 'inf_bonus', 'cor_bonus', 'cri_bonus', 'law_bonus', 'lor_bonus',
            'pro_bonus', 'soc_bonus',
        )
