from django.shortcuts import render, redirect
from Programmes.models import Programme
from .forms import RequirementForm

def parent_requirements(request):
    return render(request, 'parent_requirements.html')

def add_programme_requirement(request, programme):
    form = RequirementForm()
    programme = Programme.objects.get(id=programme)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = RequirementForm(request.POST)
        if form.is_valid():
            requirement = form.save(commit=False)
            requirement.Programme = programme
            requirement.save()
            programme.Requirements.add(requirement)
            return redirect('programme-requirements', programme=programme.id)
    else:
        return render(request, 'add_programme_requirement.html', context)