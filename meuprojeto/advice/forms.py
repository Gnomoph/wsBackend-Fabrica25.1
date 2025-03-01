from django import forms
from .models import Advice

class AdviceForm(forms.ModelForm):
    class Meta:
        model = Advice
        fields = ['text']
