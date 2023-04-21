from django.shortcuts import render
from .models import School


def school_profile(request, school):
    school = School.objects.get(id=school)
    context = {
        'school': school
    }
    return render(request, 'school_profile.html', context)

