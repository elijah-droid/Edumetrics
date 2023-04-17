from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from SchoolAdministrators.models import SchoolAdministrator
from Teachers.models import Teacher
from Parents.models import Parent
from django.contrib.auth.models import User
import random
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from SchoolAdministrators.models import Adminship
from django.utils.timezone import now
from django.core.mail import send_mail
from Students.views import generate_student_id
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def class_teacher_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.groups.filter(name='Class Teachers').exists():
            login(request, user)
            return redirect('class_teacher_dashboard')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'class_teacher_login.html', {'error_message': error_message})
    else:
        return render(request, 'class_teacher_login.html')


def parents_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        try:
            Parent.objects.get(user=user)
        except Parent.DoesNotExist:
            user = None
        if user is not None:
            login(request, user)
            request.session['base'] = 'parents_dashboard.html'
            return redirect('parent_dashboard')
        else:
            error_message = 'Invalid login credentials'
            request.session['base'] = 'parents_dashboard.html'
            return render(request, 'parent_login.html', {'error': error_message})
    else:
        return render(request, 'parent_login.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            request.session['base'] = 'user_dashboard.html'
            return redirect('user-dashboard')
        else:
            error_message = 'Invalid login credentials'
            return render(request, 'user_login.html', {'error': error_message})
    else:
        return render(request, 'user_login.html')


def student_login(request):
    if request.method == 'POST':
        # Get the email and password from the login form
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate the student's credentials
        user = authenticate(request, email=email, password=password)

        # If the student's credentials are valid, log them in and redirect to dashboard
        if user is not None and user.is_active and user.user_type == 'student':
            login(request, user)
            return redirect('student_dashboard')
        # If the student's credentials are not valid, show an error message
        else:
            error_message = 'Invalid email or password'
            return render(request, 'student_login.html', {'error_message': error_message})
    # If the request method is GET, show the login form
    else:
        return render(request, 'student_login.html')
    


def admin_login(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard')
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        try:
            SchoolAdministrator.objects.get(user=user)
        except SchoolAdministrator.DoesNotExist:
            user = None 
        if user is not None:
            login(request, user)
            request.session['base'] = 'admins_dashboard.html'
            if request.user.schooladministrator.current_school is None:
                school = random.choice(request.user.schooladministrator.schools.all())
            else: 
                school = request.user.schooladministrator.current_school
            return redirect('set-school-session', school=school.id)
        else:
            error_message = "Invalid login credentials. Please try again."
            return render(request, 'admin_login.html', {'error': error_message})

    return render(request, 'admin_login.html')


def teacher_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        try:
            teacher = Teacher.objects.get(user=user)
        except Teacher.DoesNotExist:
            user = None
        if user is not None:
            login(request, user)
            if teacher.current_profile is None:
                teacher.current_profile = random.choice(teacher.work_profile.all())
                teacher.save()
            request.session['base'] = 'teachers_dashboard.html'
            return redirect('teacher_dashboard')
        else:
            error_message = "Invalid login credentials. Please try again."
            return render(request, 'teacher_login.html', {'error': error_message})
    else:

        return render(request, 'teacher_login.html')


def set_school_session(request, school):
    user = request.user.schooladministrator
    school = user.schools.get(pk=school)
    try:
        adminship = Adminship.objects.get(Admin=request.user.schooladministrator, School=school)
        request.user.user_permissions.set(adminship.permissions.all())
        request.user.groups.set(adminship.Groups.all())
        if adminship.super_admin:
            request.user.is_superuser = True
            request.user.save()
        else:
            request.user.is_superuser = False
            request.user.save()
        adminship.last_login = now()
        adminship.save()
    except Adminship.DoesNotExist:
        request.user.user_permissions.clear()
        request.user.groups.clear()
        request.user.is_superuser = False
    user.current_school = school
    user.save()
    messages.success(request, f'You are now operating at {school}')
    recent_url = request.META.get('HTTP_REFERER')
    return redirect(recent_url)

def signup(request):
    form = UserCreationForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        first_name = request.POST['first_name']
        second_name = request.POST['second_name']
        email = request.POST['email']
        password = request.POST['password']
        code = generate_student_id()
        html_message = render_to_string('confirm_email_message.html', {'code': code})
        text_message = strip_tags(html_message)
        subject = 'Confirm Your Email Adress'
        from_email = 'edumetrics@sparklehandscs.com'
        to_email = email
        email_message = EmailMultiAlternatives(subject, text_message, from_email, [to_email])

        # Attach the HTML version of the email message
        email_message.attach_alternative(html_message, "text/html")

        # Send the email
        email_message.send()
        user = User.objects.create(
            first_name=first_name,
            last_name=second_name,
            username=email,
            email=email,
            password=password
        )
        return redirect('confirm-email', user=user.id)
    else:
        return render(request, 'signup.html', context)


def confirm_email(request, user):
    user = User.objects.get(pk=user)
    context = {
        'reg_user': user
    }
    return render(request, 'confirm_email.html', context)


def logout_view(request):
    logout(request)
    try:
        request.user.user_permissions.clear()
        request.user.is_superuser = False
        request.user.groups.clear()
        request.user.save()
    except:
        pass
    return redirect('index')

def change_password(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        if request.user.check_password(old_password):
            request.user.password = make_password(request.POST['new_password'])
            request.user.save()
            messages.success(request, 'Your password was changed successfully.')
            return redirect(request.session['next'])
    else:
        request.session['next'] = request.META.get('HTTP_REFERER')
        return render(request, 'change_password.html')
    

    