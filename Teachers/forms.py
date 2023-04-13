from django import forms
from .models import Teacher
from Classes.models import Class
from django.contrib.auth.models import User
from Subjects.models import Subject

class TeachersForm(forms.Form):

    user = forms.EmailField(
        label='''Teacher's Email''',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '''Enter Teacher's Email''',
            }
        )
    )
    
    Classes = forms.ModelMultipleChoiceField(
        queryset=Class.objects.all(),
            widget=forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                }
            )
        )
    Subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
            widget=forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                }
            )
        )