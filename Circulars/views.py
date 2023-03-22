from django.shortcuts import render
from .forms import CircularForm

def circulars(request):
    return render(request, 'circulars.html')

def add_circular(request):
    form = CircularForm()
    context = {
        'form': form
    }
    return render(request, 'add_circular.html', context)