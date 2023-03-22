from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Report
from .forms import BatchReportsForm
import random


def batch_reports(request):
    form = BatchReportsForm()
    form.fields['Exam'].queryset = request.user.schooladministrator.current_school.Examinations.all()
    form.fields['Class'].queryset = request.user.schooladministrator.current_school.classes.all()
    school = request.user.schooladministrator.current_school
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = BatchReportsForm(request.POST)
        if form.is_valid():
            cls = form.cleaned_data['Class']
            Exam = form.cleaned_data['Exam']
            students = school.students.filter(Class=cls)
            for student in students:
                report = student.Reports.create(
                    Student=student,
                    Examination=Exam,
                    Total_Score=0
                )
                for subject in student.Subjects.all():
                    report.Scores.create(
                        Report=report,
                        Subject=subject,
                        Score=0,
                    )
                Exam.Reports.add(report)
            return redirect('reports')
    else:
        return render(request, 'batch_reports.html', context)


def reports(request):
    reports = Report.objects.all()

    context = {
        'reports': reports
    }

    return render(request, 'reports.html', context)


def edit_report(request, report):
    report = Report.objects.get(pk=report)
    school = request.user.schooladministrator.current_school
    context = {
        'report': report    
    }
    if request.method == 'POST':
        for score in report.Scores.all():
            sc = request.POST[str(score.pk)]
            grade = request.POST[f'{score.pk}grade']
            grade = school.Grades.get(pk=grade)
            score.Grade = grade
            score.Score = sc
            score.save()
        report.Total_Score = sum([sc.Score for sc in report.Scores.all()])
        report.Aggregate = sum([sc.Grade.Value for sc in report.Scores.all()])
        report.save()
        return redirect(request.session['next'])
    else:
        request.session['next'] = request.META.get('HTTP_REFERER')
        return render(request, 'edit_report.html', context)


@login_required
def create_report(request):
    form = ReportForm(request.POST or None)
    if form.is_valid():
        report = form.save(commit=False)
        report.created_by = request.user
        report.save()
        messages.success(request, 'Report created successfully.')
        return redirect('report_detail', pk=report.pk)
    context = {'form': form}
    return render(request, 'create_report.html', context)


def view_report(request):
    return render(request, 'report.html')


@login_required
def delete_report(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == 'POST':
        report.delete()
        messages.success(request, 'Report deleted successfully.')
        return redirect('report_list')
    context = {'report': report}
    return render(request, 'delete_report.html', context)
