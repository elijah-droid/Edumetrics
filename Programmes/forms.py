from django import forms
from .models import Programme


class ProgrammeForm(forms.ModelForm):

    class Meta:
        model = Programme
        fields = ['Name',]
        widgets = {
            'Name': forms.Select(attrs={'class': 'form-control'}),
        }