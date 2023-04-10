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


@login_required
def school_admin_dashboard(request):
    # Get current user and school
    user = request.user

    # Get recent admin activity

    x = [cl.Name for cl in user.schooladministrator.current_school.classes.all()]
    y1 = [20, 35, 30, 25, 40]
    y2 = [15, 25, 25, 20, 35]
    

    # Create a bar chart trace
    trace1 = go.Bar(x=x, y=y1, name='Total', marker=dict(color='#103741'))
    trace2 = go.Bar(x=x, y=y2, name='Attendance')

    # Create a layout for the chart
    layout = go.Layout(title=f'{user.schooladministrator.current_school} Student Statistics', xaxis=dict(title='Classes'), yaxis=dict(title='Student'))

    # Render the chart in the template
    plot_div = plotly.offline.plot({
        "data": [trace1, trace2],
        "layout": layout
    }, output_type="div")
    admin_activity = LogEntry.objects.filter(
        content_type__app_label='app',
        action_time__gte=timezone.now() - timezone.timedelta(days=7)
    ).order_by('-action_time')[:10]                                                                                                                                                                                                   

    context = {
        'admin_activity': admin_activity,
        "plot_div": plot_div
    }

    return render(request, 'admins_dashboard.html', context)


def school_administrators(request):
    admins = Adminship.objects.filter(School=request.user.schooladministrator.current_school)
    context = {
        'admins': admins
    }
    return render(request, 'school_administrators.html', context)


def register_schooladmin(request):
    form = LinkAdminForm()
    context = {
        'form': form
    }
    return render(request, 'register_schooladmin.html', context)


def change_permissions(request, admin):
    admin = SchoolAdministrator.objects.get(pk=admin)
    permissions = Permission.objects.filter(content_type__app_label__in=my_apps)
    groups = Group.objects.all()
    context = {
        'admin': admin,
        'permissions': permissions,
        'groups': groups
    }
    if request.method == 'POST':
        permissions = request.POST.getlist('permissions')
        groups = request.POST.getlist('groups')
        groups = Group.objects.filter(id__in=groups)
        permissions = Permission.objects.filter(id__in=permissions)
        adminship = Adminship.objects.get(Admin=admin, School=request.user.schooladministrator.current_school)
        adminship.permissions.set(permissions)
        adminship.Groups.set(groups)
        return redirect('school-administrators')
    else:
        return render(request, 'change_permissions.html', context)


