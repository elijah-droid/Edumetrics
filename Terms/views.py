from django.shortcuts import render

def terms(request):
    return render(request, 'terms.html')

def add_term(request):
    pass
