from django import forms
from Classes.models import Class
from django.contrib.auth.models import User
from .models import Relationship
from .models import relationships

class ParentForm(forms.Form):

    parent = forms.EmailField(
        label='Parent Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Parent Email',
            }
        )
    )

    student = forms.CharField(
        label='Student Id',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Student Id',
            }
        )
    )


    Relationship = forms.ChoiceField(
        choices=relationships,
            widget=forms.Select(
                attrs={
                    'class': 'form-control',
                }
            )
        )