from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.decorators.cache import never_cache


class NoCacheMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        return self.get_response(request)
