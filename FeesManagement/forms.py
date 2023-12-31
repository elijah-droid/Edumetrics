from django import forms
from .models import PaymentDue, Payment

class PaymentDueForm(forms.ModelForm):
    class Meta:
        model = PaymentDue
        fields = ['Reason', 'Amount_Required', 'Classes', 'Compulsory']
        widgets = {
            'Reason': forms.TextInput(attrs={'class': 'form-control'}),
            'Amount_Required': forms.NumberInput(attrs={'class': 'form-control'}),
            'Classes': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'Compulsory': forms.CheckboxInput(attrs={'class': 'form-check-input text-nowrap'})
        }


class PaymentForm(forms.ModelForm):
    
    parent_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    payment_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Payment
        fields = ['Student', 'Method', 'Amount']
        widgets = {
            'Student': forms.Select(attrs={'class': 'form-control'}),
            'Method': forms.Select(attrs={'class': 'form-control'}),
            'Amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ParentPaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['Due', 'Amount']
        widgets = {
            'Due': forms.Select(attrs={'class': 'form-control'}),
            'Amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }
