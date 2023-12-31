from django import forms
from .models import Attendance, RollCall

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['Date', 'Class', 'Students']
        widgets = {
            'Date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'readonly': 'true'}),
            'Class': forms.Select(attrs={'class': 'form-control'}),
            'Students': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class RollCallForm(forms.ModelForm):
    class Meta:
        model = RollCall
        fields = ['Attendees',]
        widgets = {
            'Attendees': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }