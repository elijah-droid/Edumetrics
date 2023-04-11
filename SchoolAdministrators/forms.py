from django import forms
from .models import SchoolAdministrator
from django.contrib.auth.models import Permission, Group
from Edumetrics.settings import my_apps

class LinkAdminForm(forms.Form):


    

    user = forms.EmailField(
        label='User email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter User email',
            }
        )
    ) 
    Permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.filter(content_type__app_label__in=my_apps),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control',
            }
        ))

    Groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control',
            }
        ))