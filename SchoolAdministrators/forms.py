from django import forms
from .models import SchoolAdministrator
from django.contrib.auth.models import Permission
from Edumetrics.settings import my_apps

class LinkAdminForm(forms.Form):


    Permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.filter(content_type__app_label__in=my_apps),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control',
            }
        ))
    

    user = forms.IntegerField(
        label='User Id',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter User Id',
            }
        )
    ) 