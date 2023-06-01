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
from .models import PasswordReset, EmailConfirmation
from django.core.exceptions import ObjectDoesNotExist
from Students.models import Student

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
        try:
            Student.objects.get(user=user)
        except Student.DoesNotExist:
            user = None
        # If the student's credentials are valid, log them in and redirect to dashboard
        if user is not None and user.is_active and user.user_type == 'student':
            login(request, user)
            return redirect('student_dashboard')
        # If the student's credentials are not valid, show an error message
        else:
            error_message = 'Invalid email or password'
            return render(request, 'student_login.html', {'error': error_message})
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
            admin = SchoolAdministrator.objects.get(user=user)
            if admin.adminship.count() == 0:
                user = None
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
            if teacher.work_profile.count() < 1:
                user = None
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
        request.user.groups.clear()
        request.user.is_superuser = False
    user.current_school = school
    user.save()
    messages.success(request, f'You are now operating at {school}')
    recent_url = request.META.get('HTTP_REFERER')
    host = request.META.get('HTTP_HOST')
    recent_url = recent_url.replace(host, '')
    digit = False
    for char in recent_url:
        if char.isdigit():
            digit=True
    if digit:
        return redirect('admin_dashboard')
    else:
        return redirect(request.META.get('HTTP_REFERER'))

def signup(request):
    form = UserCreationForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        email = request.POST['email']
        try:
            User.objects.get(email=email)
            message = 'The email you entered is already in use.'
            messages.success(request, message)
            return redirect('.')
        except ObjectDoesNotExist:
            code = generate_student_id()
            message = f'''
                Use this code on the sign up page

                {code}
            '''
            send_mail(
                'Email Confirmation Code',
                message,
                'edumetrics@edu-metrics.com',
                [email]
            )
            try:
                confirmation = EmailConfirmation.objects.get(Email=email)
                confirmation.Code = code
                confirmation.save()
            except ObjectDoesNotExist:
                confirmation = EmailConfirmation.objects.create(Email=email, Code=code)
            return redirect('signup-details', confirmation=confirmation.id)
        return redirect('.')
    else:
        return render(request, 'signup.html', context)


def signup_details(request, confirmation):
    confirmation = EmailConfirmation.objects.get(id=confirmation)
    if request.method == 'POST':
        code = request.POST['code']
        if code == confirmation.Code:
            user = User.objects.create(
                username=confirmation.Email,
                first_name=request.POST['first_name'],
                last_name=request.POST['second_name'],
                email=confirmation.Email,
                password=make_password(request.POST['password'])
            )
            send_email(
                'Welcome To Edumetrics',
                'Your Edumetrics user account was created successfully.',
                'edumetrics@edu-metrics.com',
                [user.email]
            )
            messages.success(request, 'Account created successfully.')
            return redirect('/')
        else:
            messages.success(request, 'Invalid Code.')
            return redirect('.')
    else:
        return render(request, 'signup_details.html')


def confirm_email(request, user):
    user = User.objects.get(pk=user)
    context = {
        'reg_user': user
    }
    return render(request, 'confirm_email.html', context)


def logout_view(request):
    logout(request)
    try:
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
    

    
def forgot_password(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST['email'])
            code = generate_student_id()
            message = f'''
            Your O-T-P code is:

            {code}
            '''
            send_mail(
                'Password Reset',
                message,
                'edumetrics@sparklehandscs.com',
                [user.email],
            )
            try:
                reset = PasswordReset(User=user)
                reset.current_otp = code
                reset.save()
            except PasswordReset.DoesNotExist:
                reset = PasswordReset.objects.create(User=user, current_otp=code)
            return redirect('reset-password', reset=reset.id)
            messages.success(request, 'Code has been sent to your email')
            return redirect('.')
        except User.DoesNotExist:
            messages.success(request, 'Unknown Email')
            return redirect('.')
    return render(request, 'forgot_password.html')



def reset_password(request, reset):
    reset = PasswordReset.objects.get(id=reset)
    if request.method == 'POST':
        code = request.POST['code']
        password = request.POST['password']
        confirm = request.POST['confirm']
        if reset.current_otp == code:
            if password == confirm:
                reset.User.password = make_password(password)
                reset.User.save()
                messages.success(request, 'Password Reset Successful')
                return redirect('/')
            else:
                messages.success(request, 'Passwords Dont Match')
                return redirect('.')
        else:
            messages.success(request, 'Invalid Code')
            return redirect('.')
    else:
        return render(request, 'password_reset.html')


def teacher_switch_profile(request, profile):
    try:
        profile = request.user.teacher.work_profile.get(id=profile)
        request.user.teacher.current_profile = profile
        request.user.teacher.save()
    except ObjectDoesNotExist:
        pass
    recent_url = request.META.get('HTTP_REFERER')
    return redirect(recent_url)