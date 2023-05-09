from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from SchoolAdministrators.models import Adminship
from Schools.models import setup_steps
from django.urls import reverse




class SetUpMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.schooladministrator and request.user.has_perm('Schools.change_school'):
            if not request.user.schooladministrator.current_school.setup_step:
                request.user.schooladministrator.current_school.setup_step = setup_steps[0][0]
                request.user.schooladministrator.current_school.save()
                return redirect(setup_steps[0][0])
            elif request.user.schooladministrator.current_school.setup_step != 'Done':
                if 'Levels' not in request.path:
                    return redirect(request.user.schooladministrator.current_school.setup_step)
                else:
                    return self.get_response(request) 
        else:
            return self.get_response(request) 