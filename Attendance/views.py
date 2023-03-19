from django.shortcuts import render

def attendance(request):
    return render(request, 'attendance.html')