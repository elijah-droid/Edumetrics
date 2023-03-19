from django.shortcuts import render

def circulars(request):
    return render(request, 'circulars.html')