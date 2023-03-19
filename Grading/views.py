from django.shortcuts import render, redirect
from .forms import GradeForm, DivisionForm

def grades(request):
    return render(request, 'grades.html')

def divisions(request):
    return render(request, 'divisions.html')

def add_grade(request):
    form = GradeForm()
    form.fields['Classes'].queryset = request.user.schooladministrator.current_school.classes.all()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.School = request.user.schooladministrator.current_school
            grade.save()
            grade.Classes.set(form.cleaned_data['Classes'])
            request.user.schooladministrator.current_school.Grades.add(grade)
            return redirect('grades')
    return render(request, 'add_grade.html', context)

def add_division(request):
    form = DivisionForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = DivisionForm(request.POST)
        if form.is_valid():
            division = form.save(commit=False)
            division.School = request.user.schooladministrator.current_school
            division.save()
            division.Classes.set(form.cleaned_data['Classes'])
            request.user.schooladministrator.current_school.Divisions.add(division)
            return redirect('divisions')
    return render(request, 'add_division.html', context)