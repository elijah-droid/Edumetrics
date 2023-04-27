from django.shortcuts import render, redirect
from .forms import ProgrammeForm
from .models import Programme
from django.core.paginator import Paginator

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


def students_on_programme(request, programme):
    programme = Programme.objects.get(id=programme)
    students = programme.Students.all().order_by('active_enrollment__Date').reverse()
    paginator = Paginator(students, 6)
    page = request.GET.get('page')
    students = paginator.get_page(page)
    context = {
        'programme': programme,
        'students': students
    }
    return render(request, 'students_on_programme.html', context)


def programme_fees_structure(request, programme):
    programme = Programme.objects.get(id=programme)
    context = {
        'programme': programme
    }
    return render(request, 'programme_fees_structure.html', context)

def programme_requirments(request, programme):
    programme = Programme.objects.get(id=programme)
    context = {
        'programme': programme
    }
    return render(request, 'programme_requirements.html', context)


