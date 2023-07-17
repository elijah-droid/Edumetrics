from django.shortcuts import render, redirect
from django.http import JsonResponse


def send_message(request, ):
    if request.method == 'POST':
        data = request.POST
        return JsonResponse(data)