from django.shortcuts import render
from .models import Tally

def tallies(request):
    tallies = Tally.objects.filter(User=request.user)
    context = {
        'tallies': tallies
    }
    return render(request, 'tallies.html', context)


def tally(request):
    return render(request, 'tally.html')