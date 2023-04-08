from django import forms
from .models import SchoolAdministrator

class LinkAdminForm(forms.ModelForm):

    class Meta:
        model = SchoolAdministrator
        fields = ['permissions',]
        widgets = {
            'permissions': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


    user = forms.IntegerField(
        label='User Id',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter User Id',
            }
        )
    ) 