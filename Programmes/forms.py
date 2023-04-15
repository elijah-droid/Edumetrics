from django import forms
from .models import Programme


class ProgrammeForm(forms.ModelForm):

    class Meta:
        model = Programme
        fields = ['Name', 'Requirements']
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Requirements': forms.Textarea(attrs={'class': 'form-control'})
        }