from django import forms
from .models import Tally


class TallyForm(forms.ModelForm):

    class Meta:
        model = Tally
        fields = ['Student', 'Score']
        widgets = {
            'Student': forms.Select(attrs={'class': 'form-control mb-3'}),
            'Score': forms.NumberInput(attrs={'class': 'form-control mb-3'}),
        }