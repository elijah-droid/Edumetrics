from django import forms
from .models import Subscription
from Classes.models import Class
from Payments.models import Payment

class SubscriptionForm(forms.ModelForm):
    Parent = forms.CharField(
    label='Parent Email',
    widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Parent Email',
            }
        )
    )
    class Meta:
        model = Payment
        fields = ['amount', 'account']
        widgets = {
            'Parent': forms.Select(attrs={'class': 'form-control mt-0'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'readonly': ''}),
            'account': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'})
        }
