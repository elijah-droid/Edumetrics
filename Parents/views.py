from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.utils import timezone
from Reports.models import Report
from .models import Parent, Relationship
from .forms import ParentForm
from django.contrib.auth.models import User



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
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(id=form.cleaned_data['user'])
                try:
                    parent = Parent.objects.get(user=user)
                except Parent.DoesNotExist:
                    parent = Parent.objects.create(user=user)
                student.parents.add(parent)
                try:
                    relationship = parent.relationships.get(Child=student)
                except Relationship.DoesNotExist:
                    relationship = parent.relationships.create(Parent=parent, Child=student, Relationship=form.cleaned_data['Relationship'])
                return redirect('student-profile', student=student.id)
            except User.DoesNotExist:
                form.add_error('user', 'Invalid User Id')
                return render(request, 'link_parent.html', {'form': form})
        else:
            print(form)
    else:
        return render(request, 'link_parent.html', context)


def parent_profile(request, parent):
    parent = Parent.objects.get(pk=parent)
    