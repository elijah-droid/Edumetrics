from django import forms
from Classes.models import Class
from django.contrib.auth.models import User
from .models import Relationship
from .models import relationships

class ParentForm(forms.Form):

    email = forms.EmailField(
        label='Parent Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Parent Email',
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