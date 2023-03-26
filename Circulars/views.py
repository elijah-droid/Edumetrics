from django.shortcuts import render, redirect
from .forms import CircularForm

def circulars(request):
    return render(request, 'circulars.html')

def add_circular(request):
    form = CircularForm()
    form.fields['Classes'].queryset = request.user.schooladministrator.current_school.classes
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = CircularForm(request.POST)
        if form.is_valid():
            circular = form.save(commit=False)
            circular.School = request.user.schooladministrator.current_school
            circular.save()
            request.user.schooladministrator.current_school.Circulars.add(circular)
            return redirect('circulars')

    else:
        return render(request, 'add_circular.html', context)