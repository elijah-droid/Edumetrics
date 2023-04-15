from django import forms
from .models import Admission

class AdmissionForm(forms.ModelForm):

    class Meta:
        model = Admission
        fields = ['Student', 'Complications']
        widgets = {
            'Student': forms.Select(attrs={'class': 'form-control'}),
            'Complications': forms.Textarea(attrs={'class': 'form-control'}),
        }