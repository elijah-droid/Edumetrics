from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            return JsonResponse({'user': str(user)})
        else:
            return JsonResponse({'user': None})



def send_message(request):
    if request.method == 'POST':
        data = request.POST
        return JsonResponse(data)