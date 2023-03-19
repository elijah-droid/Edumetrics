from django import forms
from .models import Student
from Classes.models import Class
from django.contrib.auth.models import User
from Subjects.models import Subject

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'photo', 'email', 'student_id', 'date_of_birth', 'Class', 'Subjects']

    def save(self, commit=True):
        user = User.objects.create(username=self.cleaned_data['email'], email=self.cleaned_data['email'])
        student = Student.objects.create(
            user=user,
            student_id=self.cleaned_data['student_id'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            photo=self.cleaned_data['photo']
        )
        return student

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

    photo = forms.ImageField(
        label='Photo',
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email',
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

    Class = forms.ModelChoiceField(
        label='Class',
        queryset=Class.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
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