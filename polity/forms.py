from django import forms
from .models import Polity
from .models import LogEntry


class PolityForm(forms.ModelForm):

    class Meta:
        model = Polity
        fields = (
            'name', 'government', 'alignment_lc', 'alignment_ge',
            'treasury', 'unrest', 'fame', 'infamy',
            'desc',
            'tax_edict', 'promotion_edict', 'holiday_edict', 'recruitment_edict',
            'ruler_attribute_1', 'ruler_attribute_2', 'ruler_attribute_3', 'spymaster_attribute'
        )


class LogEntryForm(forms.ModelForm):

    class Meta:
        model = LogEntry
        fields = (
            'polity', 'year', 'month', 'log'
        )
