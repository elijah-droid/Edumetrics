from django import forms
from .models import Grade, Division

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['Name', 'From', 'To', 'Value', 'Classes']
        widgets = {
            'Name': forms.Select(attrs={'class': 'form-control'}),
            'From': forms.NumberInput(attrs={'class': 'form-control'}),
            'To': forms.NumberInput(attrs={'class': 'form-control'}),
            'Value': forms.NumberInput(attrs={'class': 'form-control'}),
            'Classes': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = ['Name', 'From', 'To', 'Classes']
        widgets = {
            'Name': forms.Select(attrs={'class': 'form-control'}),
            'From': forms.NumberInput(attrs={'class': 'form-control'}),
            'To': forms.NumberInput(attrs={'class': 'form-control'}),
            'Classes': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
