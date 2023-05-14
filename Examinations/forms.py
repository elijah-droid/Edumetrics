from django import forms
from .models import Examination, Paper

class ExamScheduleForm(forms.ModelForm):
    class Meta:
        model = Examination
        fields = ['Name', 'Date', 'Classes']
        widgets = {
            'Date': forms.DateInput(attrs={'type': 'Date', 'class': 'form-control'}),
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Classes': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class PaperForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = ['Subject', 'Class', 'Date', 'Time', 'Duration', 'Examiner']
        widgets = {
            'Subject': forms.Select(attrs={'class': 'form-control'}),
            'Class': forms.Select(attrs={'class': 'form-control'}),
            'Date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'Time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'Duration': forms.TextInput(attrs={'class': 'form-control'}),
            'Examiner': forms.Select(attrs={'class': 'form-control'}),
        }
