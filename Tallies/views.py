from django.shortcuts import render
from .models import Tally

def tallies(request):
    tallies = Tally.objects.filter(User=request.user)
    context = {
        'tallies': tallies
    }
    return render(request, 'tallies.html', context)


def tally(request):
    profile = request.user.teacher.current_profile
    examinations = profile.School.Examinations.filter(Classes__in=profile.Classes.all()).distinct()
    context = {
        'exams': examinations
    }
    return render(request, 'tally.html', context)