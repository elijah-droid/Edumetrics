from django import forms
from .models import Term 

class TermForm(forms.ModelForm):

    class Meta:
        model = Term
        fields = ['Name', 'From', 'To']
        widgets = {
            'Name': forms.Select(attrs={'class': 'form-control'}),
            'From': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'To': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }