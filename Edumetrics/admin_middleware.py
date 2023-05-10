from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from SchoolAdministrators.models import Adminship
from django.contrib import messages




class AdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        changed = False
        try:
            if request.user.schooladministrator:
                adminship = AdminShip.objects.get(School=request.user.schooladministrator.current_school, Admin=request.user.schooladministrator)
                if adminship.Groups.all() != request.user.groups.all():
                    adminship.Groups.set(request.user.groups.all())
                    changed = True
                if adminship.super_admin != request.user.is_superuser:
                    adminship.super_admin = request.user.is_superuser
                    adminship.save()
                    changed = True
        except:
            pass
        if changed:
            messages.success(request, 'You Pemissions were reviewed')
        return self.get_response(request)
        
    
