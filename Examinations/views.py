from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Examination
from .forms import ExamScheduleForm



@login_required
def schedule_exam(request):
    if request.method == 'POST':
        form = ExamScheduleForm(request.POST)
        if form.is_valid():
            exam_set = form.save(commit=False)
            exam_set.School = request.user.schooladministrator.current_school
            exam_set.save()
            request.user.schooladministrator.current_school.Examinations.add(exam_set)
            messages.success(request, 'Examination set scheduled successfully!')
            return redirect('examinations')
    else:
        form = ExamScheduleForm()
        form.fields['Classes'].queryset = request.user.schooladministrator.current_school.classes.all()
    context = {'form': form}
    return render(request, 'schedule_exam.html', context)


@login_required
def edit_examination_set(request, pk):
    examination_set = get_object_or_404(ExaminationSet, pk=pk)
    form = ExaminationSetForm(request.POST or None, instance=examination_set)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('examination_set_detail', pk=pk)
    context = {
        'form': form,
        'examination_set': examination_set,
    }
    return render(request, 'edit_examination_set.html', context)

@login_required
def delete_examination(request, exam):
    examination_set = get_object_or_404(Examination, pk=exam)
    examination_set.delete()
    return redirect('examinations')


def examination_list(request):
    examinations = Examination.objects.all()
    return render(request, 'examinations.html', {'examinations': examinations})


def view_exam_reports(request, exam):
    exam = Examination.objects.get(pk=exam)
    content = {
        'reports': exam.Reports.all()
    }
    return render(request, 'reports.html', content)


def assessments(request, exam):
    return render(request, 'assessments.html')