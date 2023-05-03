from django.shortcuts import render, redirect
from .forms import LevelForm


def levels(request):
    return render(request, 'levels.html')

def add_level(request):
    form = LevelForm()
    context = {
        'form': form
    }
    school = request.user.schooladministrator.current_school
    if request.method == 'POST':
        form = LevelForm(request.POST)
        level = form.save(commit=False)
        level.School = school
        level.save()
        school.Levels.add(level)
        return redirect('levels')
    else:
        return render(request, 'add_level.html', context)