from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.utils import timezone
from .models import SchoolAdministrator



@login_required
def school_admin_dashboard(request):
    # Get current user and school
    user = request.user

    # Get recent admin activity
    admin_activity = LogEntry.objects.filter(
        content_type__app_label='app',
        action_time__gte=timezone.now() - timezone.timedelta(days=7)
    ).order_by('-action_time')[:10]

    context = {
        'admin_activity': admin_activity,
    }

    return render(request, 'admins_dashboard.html', context)


def school_administrators(request):
    admins = SchoolAdministrator.objects.all()
    context = {
        'admins': admins
    }
    return render(request, 'school_administrators.html', context)


