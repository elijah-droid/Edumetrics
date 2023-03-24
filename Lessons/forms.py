from django import forms
from .models import Lesson

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['Class', 'Subject', 'Day', 'From', 'To', 'Subject', 'Teacher']
        widgets = {
            'Class': forms.Select(attrs={'class': 'form-control'}),
            'Subject': forms.Select(attrs={'class': 'form-control'}),
            'Day': forms.Select(attrs={'class': 'form-control'}),
            'From': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'To': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'Teacher': forms.Select(attrs={'class': 'form-control'})
        }
