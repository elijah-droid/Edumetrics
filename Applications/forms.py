from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ['Student',]
        widgets = {
            'Student': forms.Select(attrs={'class': 'form-control'})
        }