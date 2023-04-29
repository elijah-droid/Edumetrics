from django import forms
from .models import Class
from Schools.models import School

class ClassForm(forms.ModelForm):

    class Meta:
        model = Class
        fields = ['Name', 'Index', 'Class_Teacher', 'From', 'To']
        widgets = {
            'Name': forms.Select(attrs={'class': 'form-control'}),
            'Index': forms.NumberInput(attrs={'class': 'form-control', 'readonly': ''}),
            'Class_Teacher': forms.Select(attrs={'class': 'form-control'}),
            'From': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'To': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }
    