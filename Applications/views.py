from django.shortcuts import render, redirect
from Schools.models import School
from .forms import ApplicationForm
from django.core.mail import send_mail

def  schools_listing(request):
    schools = School.objects.all()
    context = {
        'schools': schools
    }
    return render(request, 'schools_listing.html', context)


def apply(request, school):
    form = ApplicationForm()
    school = School.objects.get(id=school)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.Parent = request.user.parent
            application.School = school
            application.save()
            school.Applications.add(application)
            request.user.parent.applications.add(application)
            return redirect('parent-applications')
    else:
        return render(request, 'apply.html', context)


def parent_applications(request):
    return render(request, 'parent_applications.html')


def school_applications(request):
    return render(request, 'school_applications.html')


def applicant_profile(request, application):
    application = request.user.schooladministrator.current_school.Applications.get(pk=application)
    context = {
        'application': application
    }
    return render(request, 'applicant_profile.html', context)


def approve_application(request, application):
    application = request.user.schooladministrator.current_school.Applications.get(id=application)
    application.status = 'Approved'
    application.save()
    email = application.Parent.user.email
    message = f'''
    The application you sent to {request.user.schooladministrator.current_school}.
    Was finally approved.
    You are free to visit the administration offices to summarise the process.
    '''
    send_mail(
        'Application Approved',
        message,
        'edumetrics@sparklehandscs.com',
        [email]
    )
    return redirect('school-applications')