from django.shortcuts import render, redirect
from .forms import AttendanceForm, RollCallForm
from django.utils.timezone import now
from django.utils import timezone
from .models import Attendance
from Lessons.models import Lesson
from django.contrib import messages
from django.core.mail import send_mail

def attendance(request):
    return render(request, 'attendance.html')

def add_attenance(request):
    form = AttendanceForm(initial={'Date': now()})
    print(timezone.get_current_timezone())
    attendance = Attendance.objects.filter(Date=now())
    form.fields['Class'].queryset = request.user.schooladministrator.current_school.classes.exclude(pk__in=attendance.values('Class__id'))
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            clas = form.cleaned_data['Class']
            number = form.cleaned_data['Students']
            if clas.Students.count() >= number:
                attendance = form.save(commit=False)
                attendance.School = request.user.schooladministrator.current_school
                attendance.save()
                request.user.schooladministrator.current_school.attendance.add(attendance)
                return redirect('attendance')
            else:
                messages.success(request, 'The number cannot the number of students in the class')
                return redirect('.')
    return render(request, 'add_attendance.html', context)


def roll_call(request, lesson):
    lesson = Lesson.objects.get(pk=lesson)
    form = RollCallForm()
    form.fields['Attendees'].queryset = request.user.schooladministrator.current_school.students.filter(Class=lesson.Class, Subjects=lesson.Subject)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = RollCallForm(request.POST)
        if form.is_valid():
            attendees = form.cleaned_data['Attendees']
            students = request.user.schooladministrator.current_school.students.filter(Class=lesson.Class, Subjects=lesson.Subject)
            missed = [st for st in students if st not in attendees]
            for s in missed:
                emails = [p.user.email for p in s.parents.all()]
                print(emails)
                message = f'''
                {s} missed a {lesson.Subject} lesson today,

                Please find out why.
                '''
                send_mail(
                    'Lesson Missed',
                    message,
                    'edumetrics@edu-metrics.com',
                    [emails]
                )
    return render(request, 'roll_call.html', context)