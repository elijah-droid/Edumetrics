from django.shortcuts import render

def enrollments(request):
    return render(request, 'enrollments.html')

