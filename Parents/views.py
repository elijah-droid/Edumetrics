from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.utils import timezone
from Reports.models import Report
from .models import Parent
from .forms import ParentForm


@login_required
def parent_dashboard(request):
    parent = request.user.parent
    reports = Report.objects.filter(Student__in=parent.children.all())
    content = {
        'reports': reports
    }
    return render(request, 'parents_dashboard.html', content)


@login_required
def parents_list(request):
    parents = Parent.objects.all()
    content = {
        'parents': parents
    }
    return render(request, 'parents_list.html', content)


@login_required
def link_parent(request, student):
    form = ParentForm()
    student = request.user.schooladministrator.current_school.students.get(pk=student)
    context = {
        'form': form,
        'student': student
    }
    return render(request, 'link_parent.html', context)