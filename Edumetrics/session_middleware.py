from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages




class SessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_login = request.user.last_login
            current_time = timezone.now()
            session_duration = current_time - last_login
            session_duration_in_seconds = session_duration.total_seconds()
            session_duration_in_minutes = session_duration_in_seconds / 60
            session_duration = session_duration_in_minutes / 60
            print(session_duration)
            if session_duration >= 12:
                logout(request)
                messages.success(request, 'You will have to login again')
                return redirect('/')
        if str(request.user) != 'AnonymousUser' and '/admin/' not in request.path:
            if request.session.get('base') == 'base.html':
                if str(request.user) != 'AnonymousUser':
                    logout(request)
                    return redirect('/')
                else:
                    return self.get_response(request)
            else:
                return self.get_response(request)
        else:
            return self.get_response(request)

        
    
