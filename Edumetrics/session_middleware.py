from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect




class SessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
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

        
    
