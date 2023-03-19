from django.shortcuts import render,redirect
from .forms import ClassForm

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