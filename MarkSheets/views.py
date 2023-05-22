from django.shortcuts import render, redirect
from .models import MarkSheet
from .forms import MarkSheetForm
from Tallies.forms import TallyForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from Examinations.models import Paper


def marksheets(request):
    papers = Paper.objects.filter(Examiner=request.user.teacher)
    context = {
        'papers': papers
    }
    return render(request, 'marksheets.html', context)


def marksheet_tallies(request, marksheet):
    marksheet = MarkSheet.objects.get(pk=marksheet)
    context = {
        'marksheet': marksheet
    }
    return render(request, 'marksheet_tallies.html', context)


def create_marksheet(request):
    context = {
        'form': MarkSheetForm()
    }
    if request.method == 'POST':
        form = MarkSheetForm(request.POST)
        if form.is_valid():
            try:
                sheet = MarkSheet.objects.get(Exam=form.cleaned_data['Exam'], Class=form.cleaned_data['Class'], Subject=form.cleaned_data['Subject'])
                messages.success(request, 'The Marksheet Is Already Available')
            except MarkSheet.DoesNotExist:
                sheet = request.user.teacher.current_profile.School.mark_sheets.create(Exam=form.cleaned_data['Exam'], Class=form.cleaned_data['Class'], Subject=form.cleaned_data['Subject'])
                messages.success(request, 'The Marksheet has been created successfully')
            return redirect('marksheet-tallies', marksheet=sheet.id)

    else:
        return render(request, 'create_marksheet.html', context)


def add_score(request, marksheet):
    marksheet = MarkSheet.objects.get(pk=marksheet)
    form = TallyForm()
    context = {
        'marksheet': marksheet,
        'form': form
    }
    if request.method == 'POST':
        form = TallyForm(request.POST)
        if form.is_valid():
            try:
                tally = marksheet.Tallies.get(Student=form.cleaned_data['Student'])
                tally = TallyForm(request.POST, instance=tally)
                tally = tally.save()
            except ObjectDoesNotExist:
                tally = form.save()
                marksheet.Tallies.add(tally)
            try:
                report = request.user.teacher.current_profile.School.Reports.get(Student=tally.Student, Examination=marksheet.Exam)
            except ObjectDoesNotExist:
                report = request.user.teacher.current_profile.School.Reports.create(Student=tally.Student, Examination=marksheet.Exam)
            try:
                score = report.Scores.get(Subject=marksheet.Subject, Report=report)
            except ObjectDoesNotExist:
                score = report.Scores.create(Subject=marksheet.Subject, Report=report, Score=tally.Score)
            score.Score = tally.Score
            grade = request.user.teacher.current_profile.School.Grades.get(From__lte=tally.Score, To__gte=tally.Score)
            tally.Grade = grade
            tally.save()
            score.Grade = grade
            score.save()
            report.Total_Score = report.Scores.aggregate(total=Sum('Score'))['total']
            report.save()
            return redirect('marksheet-tallies', marksheet=marksheet.pk)
    else:
        return render(request, 'marksheet_addscore.html', context)

def exam_marksheets(request, exam):
    exam = request.user.schooladministrator.current_school.Examinations.get(id=exam)
    context = {
        'exam': exam
    }
    return render(request, 'exam_marksheets.html', context)