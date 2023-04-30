from django.shortcuts import render, redirect
from django.contrib.auth.models import Permission, Group
from django.contrib.auth.decorators import login_required
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.utils import timezone
from .models import SchoolAdministrator, Adminship
import plotly.graph_objs as go
import plotly
from .forms import LinkAdminForm
from Edumetrics.settings import my_apps
from Classes.templatetags import classfilters
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

@login_required
def school_admin_dashboard(request):
    # Get current user and school
    user = request.user

    # Get recent admin activity

    x = [cl.Name for cl in user.schooladministrator.current_school.classes.all()]
    y1 = [cl.Students.count() for cl in user.schooladministrator.current_school.classes.all()]
    y2 = [classfilters.attendance(cl, request) for cl in user.schooladministrator.current_school.classes.all()]
    

    # Create a bar chart trace
    trace1 = go.Bar(x=x, y=y1, name='Total', marker=dict(color='#103741'))
    trace2 = go.Bar(x=x, y=y2, name='Attendance')

    # Create a layout for the chart
    layout = go.Layout(title=f'Student Statistics', xaxis=dict(title='Classes'), yaxis=dict(title='Student'))

    # Render the chart in the template
    plot_div = plotly.offline.plot({
        "data": [trace1, trace2],
        "layout": layout
    }, output_type="div")
    labels = ['Paid', 'Unpaid']
    values = [20, 50]
    colors = ['#FE5D37', '#103741']
    trace = go.Pie(labels=labels, values=values, marker=dict(colors=colors))
    layout = go.Layout(title='Fees Payments')
    chart = plotly.offline.plot({'data': [trace], 'layout': layout}, output_type='div')
    labels = ['Paid', 'Unpaid']
    expected = request.user.schooladministrator.current_school.Dues.filter(Compulsory=True).aggregate(total=Sum('Amount_Required'))['total']
    if expected:
        pass
    else:
        expected = 0
    expected_pay = expected * request.user.schooladministrator.current_school.students.count()
    students = request.user.schooladministrator.current_school.students.count()
    percentage = int(students/2)*expected
    percentage = (percentage/expected_pay) * 100
    values = [percentage, 100-percentage]
    colors = ['#FE5D37', '#103741']
    trace = go.Pie(labels=labels, values=values, marker=dict(colors=colors))
    layout = go.Layout(title='Fees Payments')
    chart = plotly.offline.plot({'data': [trace], 'layout': layout}, output_type='div')
    admin_activity = LogEntry.objects.filter(
        content_type__app_label='app',
        action_time__gte=timezone.now() - timezone.timedelta(days=7)
    ).order_by('-action_time')[:10]                                                                                                                                                                                                   

    context = {
        'admin_activity': admin_activity,
        "plot_div": plot_div,
        'plot2': chart,
    }

    return render(request, 'admins_dashboard.html', context)


def school_administrators(request):
    admins = Adminship.objects.filter(School=request.user.schooladministrator.current_school)
    context = {
        'admins': admins
    }
    return render(request, 'school_administrators.html', context)


def teacher_administrators(request):
    return render(request, 'teacher_administrators.html')


def register_schooladmin(request):
    form = LinkAdminForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = LinkAdminForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(email=form.cleaned_data['email'])
                try:
                    admin = SchoolAdministrator.objects.get(user=user)
                    if admin in request.user.schooladministrator.current_school.Administrators.all():
                        messages.success(request, 'This user is already a school admin in this school')
                        return redirect('.')
                except ObjectDoesNotExist:
                    admin = SchoolAdministrator.objects.create(user=user)
                adminship = form.save(commit=False)
                adminship.School = request.user.schooladministrator.current_school
                adminship.Admin = admin
                adminship.save()
                admin.adminship.add(adminship)
                messages.success(request, 'School Administrator has been linked successfully.')
                return redirect('school-administrators')
            except User.DoesNotExist:
                messages.success(request, 'Unregistered Email')
                return redirect('.')
        else:
            print(form)
    else:
        return render(request, 'register_schooladmin.html', context)


def change_permissions(request, admin):
    admin = SchoolAdministrator.objects.get(pk=admin)
    adminship = admin.adminship.get(School=request.user.schooladministrator.current_school, Admin=admin)
    form = LinkAdminForm(instance=adminship)
    del form.fields['email']
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = LinkAdminForm(request.POST, instance=adminship)
        del form.fields['email']
        if form.is_valid():
            form.save()
        return redirect('school-administrators')
    else:
        return render(request, 'change_permissions.html', context)


def terminate_admin(request, adminship):
    adminship = Adminship.objects.get(id=adminship)
    context = {
        'adminship': adminship
    }
    if request.method == 'POST':
        answer = request.POST['answer']
        if answer == 'yes':
            adminship.delete()
            messages.success(request, 'Admin was terminated successfully.')
            return redirect('school-administrators')
        else:
            messages.success(request, 'Termination Cancelled')
            return redirect('school-administrators')
    else:
        return render(request, 'terminate_admin.html', context)


