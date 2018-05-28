from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = (
            'name', 'desc', 'polity', 'eco_bonus', 'loy_bonus', 'sta_bonus',
            'fam_bonus', 'inf_bonus', 'cor_bonus', 'cri_bonus',
            'law_bonus', 'lor_bonus', 'pro_bonus', 'soc_bonus',
        )
