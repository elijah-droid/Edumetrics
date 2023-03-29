from django import forms
from Classes.models import Class
from django.contrib.auth.models import User
from .models import Relationship
from .models import relationships

class ParentForm(forms.Form):

    user = forms.IntegerField(
        label='Parent User Id',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Parent User Id',
            }
        )
    )

    Relationship = forms.MultipleChoiceField(
        choices=relationships,
            widget=forms.Select(
                attrs={
                    'class': 'form-control',
                }
            )
        )