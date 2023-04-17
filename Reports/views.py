from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Report
from .forms import BatchReportsForm, PublishBatchReportsForm
import random
from django.urls import reverse
from Students.models import Student
from Examinations.models import Examination
import docx


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
                try:
                    Report.objects.get(Student=student, Examination=Exam)
                except Report.DoesNotExist:
                    report = student.Reports.create(
                        Student=student,
                        Examination=Exam,
                        Total_Score=0
                    )
                    school.Reports.add(report)
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


def student_reports(request, student):
    student = Student.objects.get(id=student)
    context = {
        'student': student
    }
    return render(request, 'student_reports.html', context)


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


def create_report(request, student, examination):
    student = Student.objects.get(pk=student)
    exam = Examination.objects.get(pk=examination)
    report = student.Reports.create(Student=student, Examination=exam)
    for subject in student.Subjects.all():
        report.Scores.create(Score=0, Report=report, Subject=subject)
    student.school.Reports.add(report)
    return redirect('edit-report', report=report.id)


def download_report(request, report):
    report = Report.objects.get(pk=report)
    doc = docx.Document()
    for clas in request.user.schooladministrator.current_school.classes.all():
        doc.add_heading(f'{report.student} {report.student.Examination} Reports', level=1).alignment = WD_ALIGN_PARAGRAPH.CENTER
        doc.add_paragraph()
        table = doc.add_table(rows=report.Student.Subjects.count()+4, cols=4)
        table.cell(0, 0).text = 'Subject'
        table.cell(0, 1).text = 'Marks'
        cl = 1
        for score in report.Scores.all():
            table.cell(0, cl).text = score.Subject.name
            cl+=1
        doc.add_page_break()

    document_io = io.BytesIO()
    doc.save(document_io)
    document_io.seek(0)
    response = FileResponse(document_io, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename="{request.user.schooladministrator.current_school}_{exam}_assessment_sheets.docx"'
    return response

def publish_batch(request):
    context = {
        'form': PublishBatchReportsForm()
    }
    if request.method == 'POST':
        form = PublishBatchReportsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            reports = request.user.schooladministrator.current_school.Reports.filter(Student__Class=data['Class'], Examination=data['Exam'])
            reports.update(Published=True)
            return redirect('reports')
    else:
        return render(request, 'publish_batch.html', context)


def child_reports(request):
    return render(request, 'child_reports.html')