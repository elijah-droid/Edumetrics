from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.mail import send_mail
import os
from Students.models import Student
from django.contrib import messages


def get_image(request, student):
    student = Student.objects.get(id=student)
    if student.photo:
        image_path = student.photo.path
    else:
        image_path = 'Edumetrics/static/img/user_.png'
    with open(image_path, 'rb') as f:
        image_data = f.read()
    return HttpResponse(image_data, content_type='image/png')



def index(request):
    return render(request, 'index.html')


def user_dashboard(request):
    return render(request, 'user_dashboard.html')

def email_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        send_mail(
            f'Email From {request.user.schooladministrator.current_school}',
            request.POST['message'],
            'edumetrics@sparklehandscs.com',
            [user.email],
            fail_silently=False
        )
        messages.success(request, 'Email sent successfully')
        recent_url = request.META.get('HTTP_REFERER')
        return redirect(recent_url)
    else:
        return render(request, 'email_user.html')

def email_sent(request):
    return render(request, 'email_sent.html')


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

    