from django.shortcuts import render,redirect
from .forms import ClassForm
import plotly.graph_objs as go
import plotly
from Classes.models import Class

def classes(request):
    return render(request, 'classes.html')

def add_class(request):
    form = ClassForm()
    content = {
        'form': form
    }
    if request.method == 'POST':
        form = ClassForm(request.POST)
        cls = form.save(commit=False)
        cls.School = request.user.schooladministrator.current_school
        cls.save()
        request.user.schooladministrator.current_school.classes.add(cls)
        return redirect('classes')
    else:
        return render(request, 'add_class.html', content)


def class_performance(request, clas):
    x = [subject.name for subject in request.user.schooladministrator.current_school.Subjects.all()]
    y = [20, 35, 30, 25, 40]
    clas = Class.objects.get(pk=clas)
    # Create a bar chart trace
    trace1 = go.Bar(x=x, y=y, name='Average Score', marker=dict(color='#103741'))

    # Create a layout for the chart
    layout = go.Layout(title=f'{clas.Name} Average Performance Statistics', xaxis=dict(title='Subjects'), yaxis=dict(title='Average Score'))

    # Render the chart in the template
    plot_div = plotly.offline.plot({
        "data": [trace1],
        "layout": layout
    }, output_type="div")
    context = {
        'graph': plot_div
    }
    return render(request, 'class_performance.html', context)


def class_students(request, clas):
    clas = request.user.schooladministrator.current_school.classes.get(id=clas)
    context = {
        'class': clas
    }
    return render(request, 'class_students.html', context)

def class_streams(request, clas):
    clas = request.user.schooladministrator.current_school.classes.get(id=clas)
    context = {
        'class': clas
    }
    return render(request, 'class_streams.html', context)


def class_profile(request, clas):
    clas = request.user.schooladministrator.current_school.classes.get(id=clas)
    context = {
        'class': clas
    }
    return render(request, 'class_profile.html', context)