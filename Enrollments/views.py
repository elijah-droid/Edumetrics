from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def enrollments(request):
    return render(request, 'enrollments.html')

