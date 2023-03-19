from django import forms
from .models import Teacher
from Classes.models import Class
from django.contrib.auth.models import User
from Subjects.models import Subject

class TeachersForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['user',]


    user = forms.IntegerField(
        label='User Id',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter User Id',
            }
        )
    )