from django import forms
from .models import PaymentDue, Payment

class PaymentDueForm(forms.ModelForm):
    class Meta:
        model = PaymentDue
        fields = ['Reason', 'Amount_Required', 'Classes']
        widgets = {
            'Reason': forms.TextInput(attrs={'class': 'form-control'}),
            'Amount_Required': forms.NumberInput(attrs={'class': 'form-control'}),
            'Classes': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['parent', 'Student', 'Due', 'Method', 'Amount']
        widgets = {
            'parent': forms.Select(attrs={'class': 'form-control'}),
            'Student': forms.Select(attrs={'class': 'form-control'}),
            'Due': forms.Select(attrs={'class': 'form-control'}),
            'Method': forms.Select(attrs={'class': 'form-control'}),
            'Amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }
