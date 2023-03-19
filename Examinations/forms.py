from django import forms
from .models import Examination

class ExamScheduleForm(forms.ModelForm):
    class Meta:
        model = Examination
        fields = ['Name', 'Date', 'Classes']
        widgets = {
            'Date': forms.DateInput(attrs={'type': 'Date', 'class': 'form-control'}),
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Classes': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
