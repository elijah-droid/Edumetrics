from django import forms
from .models import MarkSheet


class MarkSheetForm(forms.ModelForm):

    class Meta:
        model = MarkSheet
        fields = ['Exam', 'Class', 'Subject']
        widgets = {
            'Exam': forms.Select(attrs={'class': 'form-control'}),
            'Class': forms.Select(attrs={'class': 'form-control'}),
            'Subject': forms.Select(attrs={'class': 'form-control'})
        }
        