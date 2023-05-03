from django import forms
from .models import Subject
from Schools.models import School

class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ['name', 'Head_Of_Department', 'Levels']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'Head_Of_Department': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Optional'}),
            'Levels': forms.SelectMultiple(attrs={'class': 'form-control'})
        }
    