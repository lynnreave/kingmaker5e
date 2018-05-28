from django import forms
from .models import DiplomaticRelation


class DiplomaticRelationForm(forms.ModelForm):

    class Meta:
        model = DiplomaticRelation
        fields = (
            'holder', 'target', 'attitude', 'treaties', 'size', 'economy', 'stability'
        )
