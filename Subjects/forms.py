from django import forms
from .models import Subject, Combination
from Schools.models import School

class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ['name', 'Head_Of_Department', 'Levels', 'Type']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'Head_Of_Department': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Optional'}),
            'Levels': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'Type': forms.Select(attrs={'class': 'form-control'})
        }
    

class CombinationForm(forms.ModelForm):

    class Meta:
        model = Combination
        fields = ['Principals', 'Subsidiary',]
        widgets = {
            'Principals': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'Subsidiary': forms.Select(attrs={'class': 'form-control'}),
        }