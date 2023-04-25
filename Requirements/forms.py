from django import forms
from .models import Requirement



class RequirementForm(forms.ModelForm):

    class Meta:
        model = Requirement
        fields = ['Name', 'Quantity']
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Quantity': forms.TextInput(attrs={'class': 'form-control'}),
        }