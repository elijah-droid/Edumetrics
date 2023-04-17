from django import forms
from Examinations.models import Examination
from Classes.models import Class

class BatchReportsForm(forms.Form):
    Exam = forms.ModelChoiceField(queryset=Examination.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    Class = forms.ModelChoiceField(queryset=Class.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))


class PublishBatchReportsForm(forms.Form):
    Exam = forms.ModelChoiceField(queryset=Examination.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    Class = forms.ModelChoiceField(queryset=Class.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    Paid_Percentage = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))