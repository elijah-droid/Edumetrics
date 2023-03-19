from django import forms
from .models import Event
from Classes.models import Class

class ScheduleEventForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    Classes = forms.ModelMultipleChoiceField(queryset=Class.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    start_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))
    end_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))

    class Meta:
        model = Event
        fields = ['title', 'description', 'Classes', 'start_time', 'end_time']