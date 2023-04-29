from django import forms
from .models import Level



class LevelForm(forms.ModelForm):

    class Meta:
        model = Level
        fields = ['Name', 'Classes', 'Subjects']
        widgets = {
            'Name': forms.Select(attrs={'class': 'form-control'}),
            'Classes': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'Subjects': forms.SelectMultiple(attrs={'class': 'form-control'})
        }