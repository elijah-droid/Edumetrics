from django import forms
from .models import SchoolAdministrator, Adminship
from django.contrib.auth.models import Permission, Group
from Edumetrics.settings import my_apps

class LinkAdminForm(forms.ModelForm):

    email = forms.EmailField(
        label='''Admin's Email''',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '''Enter Administrator's Email''',
            }
        )
    )
    
    class Meta:
        model = Adminship
        fields = ['Groups', 'super_admin']
        widgets = {
            'Groups': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'super_admin': forms.CheckboxInput(attrs={'class': 'form-check-input text-nowrap'})
        }
