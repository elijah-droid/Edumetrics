from django import forms
from .models import Level



class LevelForm(forms.ModelForm):

    class Meta:
        model = Level
        fields = ['Name',]
        widgets = {
            'Name': forms.Select(attrs={'class': 'form-control'}),
        }