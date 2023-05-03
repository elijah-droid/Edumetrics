from django import forms
from .models import Student
from Classes.models import Class
from django.contrib.auth.models import User
from Subjects.models import Subject

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'photo', 'student_id', 'Stream', 'Programme', 'date_of_birth', 'Combination', 'Subjects']
        widgets = {
            'Programme': forms.Select(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'Combination': forms.Select(attrs={'class': 'form-control'}),
            'Stream': forms.Select(attrs={'class': 'form-control'}),
        }


    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name',
            }
        )
    )

    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name',
            }
        )
    )

    student_id = forms.CharField(
        label='Student Id',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Student Id',
                'readonly': 'true'
            }
        )
    )

    date_of_birth = forms.DateField(
        label='Date of Birth',
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Enter Date Born',
            }
        )
    )

    Subjects = forms.ModelMultipleChoiceField(
        label='Subjects',
        queryset=Subject.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control',
            }
        )
    )

    error_messages = {
        'required': ''
    }