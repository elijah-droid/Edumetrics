from django.shortcuts import render
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from django.conf import settings

def index(request):
    return render(request, 'index.html')


def user_dashboard(request):
    return render(request, 'user_dashboard.html')