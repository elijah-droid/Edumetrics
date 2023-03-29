from django import forms
from .models import Subscription
from Classes.models import Class

class SubscriptionForm(forms.ModelForm):
    Parent = forms.CharField(
    label='Parent Id',
    widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Parent User Id',
            }
        )
    )
    class Meta:
        model = Subscription
        fields = ['Amount', 'Method']
        widgets = {
            'Parent': forms.Select(attrs={'class': 'form-control mt-0'}),
            'Amount': forms.Select(attrs={'class': 'form-control'}),
            'Method': forms.Select(attrs={'class': 'form-control'})
        }
