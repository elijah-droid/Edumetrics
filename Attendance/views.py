from django.shortcuts import render, redirect
from .forms import AttendanceForm
from django.utils.timezone import now
from django.utils import timezone
from .models import Attendance

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
            attendance = form.save(commit=False)
            attendance.School = request.user.schooladministrator.current_school
            attendance.save()
            request.user.schooladministrator.current_school.attendance.add(attendance)
            return redirect('attendance')
    return render(request, 'add_attendance.html', context)