from Streams.models import Stream
from django import forms


class StreamForm(forms.ModelForm):

    class Meta:
        model = Stream
        fields = ['Name', 'Class_Teacher']
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Class_Teacher': forms.Select(attrs={'class': 'form-control'})
        }