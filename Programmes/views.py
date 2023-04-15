from django.shortcuts import render, redirect
from .forms import ProgrammeForm

def programmes(request):
    return render(request, 'programmes.html')

def add_programme(request):
    context = {
        'form': ProgrammeForm()
    }
    if request.method == 'POST':
        form = ProgrammeForm(request.POST)
        if form.is_valid():
            programme = form.save(commit=False)
            programme.School = request.user.schooladministrator.current_school
            programme.save()
            programme.School.Programmes.add(programme)
            return redirect('programmes')
    else:
        return render(request, 'add_programme.html', context)