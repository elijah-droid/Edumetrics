from django.shortcuts import render
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from django.conf import settings

def index(request):
    return render(request, 'index.html')


def user_dashboard(request):
    return render(request, 'user_dashboard.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def about_us(request):
    return render(request, 'about.html')

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

def handler403(request, exception):
    return render(request, '403.html', status=403)

    