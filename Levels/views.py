from django.shortcuts import render
from .forms import LevelForm


def levels(request):
    return render(request, 'levels.html')

def add_level(request):
    form = LevelForm()
    context = {
        'form': form
    }
    school = request.user.schooladministrator.current_school
    form.fields['Classes'].queryset = school.classes.all()
    form.fields['Subjects'].queryset = school.Subjects.all()
    return render(request, 'add_level.html', context)