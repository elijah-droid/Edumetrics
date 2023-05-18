from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Subject
from .forms import SubjectForm, CombinationForm

def add_subject(request):
    form = SubjectForm()
    form.fields['Levels'].queryset = request.user.schooladministrator.current_school.Levels.all()
    form.fields['name'].choices = ((s[0], s[0])  for s in form.fields['name'].choices if s[0] not in [subject.name for subject in request.user.schooladministrator.current_school.Subjects.all()])
    form.fields['Head_Of_Department'].queryset = request.user.schooladministrator.current_school.Teachers.all()
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.School = request.user.schooladministrator.current_school
            subject.save()
            subject.Levels.set(form.cleaned_data['Levels'])
            for level in subject.Levels.all():
                level.Subjects.add(subject)
            request.user.schooladministrator.current_school.Subjects.add(subject)
            messages.success(request, 'Subject created successfully.')
            return redirect('subjects')
    else:
        return render(request, 'add_subject.html', {'form': form})

def edit_subject(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subject updated successfully.')
            return redirect('subjects')
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'edit_subject.html', {'form': form, 'subject': subject})

def delete_subject(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    subject.delete()
    messages.success(request, 'Subject deleted successfully.')
    return redirect('subjects')

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects.html', {'subjects': subjects})


def combinations(request):
    return render(request, 'combinations.html')

def add_combination(request):
    form = CombinationForm()
    form.fields['Principals'].queryset = request.user.schooladministrator.current_school.Subjects.filter(Levels__Name='Secondary Advanced Level', Type='Compulsory')
    form.fields['Subsidiary'].queryset = request.user.schooladministrator.current_school.Subjects.filter(Levels__Name='Secondary Advanced Level', Type='Optional')
    context = {
        'form': form
    }
    return render(request, 'add_combination.html', context)