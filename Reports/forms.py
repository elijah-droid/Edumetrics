from django import forms
from Examinations.models import Examination
from Classes.models import Class

class BatchReportsForm(forms.Form):
    Exam = forms.ModelChoiceField(queryset=Examination.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    Class = forms.ModelChoiceField(queryset=Class.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
