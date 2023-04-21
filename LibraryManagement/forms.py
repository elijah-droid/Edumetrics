from django import forms
from .models import Book, LendOut


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['Name', 'Number', 'For_Classes']
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Number': forms.NumberInput(attrs={'class': 'form-control'}),
            'For_Classes': forms.SelectMultiple(attrs={'class': 'form-control'})
        }


class LendOutForm(forms.ModelForm):

    class Meta:
        model = LendOut
        fields = ['Student', 'Number']
        widgets = {
            'Student': forms.Select(attrs={'class': 'form-control'}),
            'Number': forms.NumberInput(attrs={'class': 'form-control'})
        }