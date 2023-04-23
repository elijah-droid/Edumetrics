from django import forms
from .models import PastPaper

class PastPaperForm(forms.ModelForm):
    
    class Meta:
        model = PastPaper
        fields = ['Class', 'Subject']
        widgets = {
            'Class': forms.Select(attrs={'class': 'form-control'}),
            'Subject': forms.Select(attrs={'class': 'form-control'})
        }