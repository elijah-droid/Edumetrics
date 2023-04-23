from django import forms
from .models import PastPaper

class PastPaperForm(forms.ModelForm):
    
    class Meta:
        model = PastPaper
        fields = ['Class', 'Subject', 'Questions_Pdf', 'Answers_Pdf', 'Description', 'Price']
        widgets = {
            'Class': forms.Select(attrs={'class': 'form-control'}),
            'Subject': forms.Select(attrs={'class': 'form-control'}),
            'Questions_Pdf': forms.FileInput(attrs={'class': 'form-control'}),
            'Answers_Pdf': forms.FileInput(attrs={'class': 'form-control'}),
            'Description': forms.Textarea(attrs={'class': 'form-control'}),
            'Price': forms.NumberInput(attrs={'class': 'form-control'})
        }