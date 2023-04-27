from django.shortcuts import render, redirect
from .forms import GradeForm, DivisionForm
from django.contrib.auth.decorators import permission_required
import plotly.graph_objs as go
import plotly
from Reports.models import Score


@permission_required('Grading.can_view_grade', raise_exception=True)
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
            scores = Score.objects.filter(Report__Examination__School=request.user.schooladministrator.current_school, Report__Published=False, Score__lte=grade.To, Score__gte=grade.From).update(Grade=grade)
            return redirect(request.session['next'])
    request.session['next'] = request.META.get('HTTP_REFERER')
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

def division_stats(request, division):
    division = request.user.schooladministrator.current_school.Divisions.get(id=division)
    x = [exam.Name for exam in request.user.schooladministrator.current_school.Examinations.all()[:3]]
    y1 = [20, 35, 30, 25, 40]
    

    # Create a bar chart trace
    trace2 = go.Bar(x=x, y=y1, name=division.Name)

    # Create a layout for the chart
    layout = go.Layout(title=f'{division.Name} Statistics', xaxis=dict(title='Last Three Sets'), yaxis=dict(title=f'Number of {division.Name}s'))

    # Render the chart in the template
    plot_div = plotly.offline.plot({
        "data": [trace2],
        "layout": layout
    }, output_type="div")
    context = {
        'graph': plot_div
    }
    return render(request, 'division_stats.html', context)