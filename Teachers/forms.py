from django import forms
from .models import Teacher, WorkProfile
from Classes.models import Class
from django.contrib.auth.models import User
from Subjects.models import Subject

class TeachersForm(forms.ModelForm):

    class Meta:
        model = WorkProfile
        fields = ['Classes', 'Subjects']
        widgets = {
            'Classes': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'Subjects': forms.SelectMultiple(attrs={'class': 'form-control'})
        }


    email = forms.EmailField(
        label='''Teacher's Email''',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '''Enter Teacher's Email''',
            }
        )
    )