from django import forms
from .models import Circular

class CircularForm(forms.ModelForm):
    class Meta:
        model = Circular
        fields = ['title', 'body', 'Classes']
        widgets = {
            'title': forms.DateInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'Classes': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
