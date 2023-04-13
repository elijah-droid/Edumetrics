from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.mail import send_mail



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
        return redirect('email-sent')
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

    