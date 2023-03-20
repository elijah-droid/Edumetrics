from django.shortcuts import render

def attendance(request):
    return render(request, 'attendance.html')

def add_attenance(request):
    return render(request, 'add_attendance.html')