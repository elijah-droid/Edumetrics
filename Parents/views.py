from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.utils import timezone
from Reports.models import Report
from .models import Parent, Relationship
from .forms import ParentForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from Students.views import generate_student_id
from Auth.models import TelConfirmation



@login_required
def parent_dashboard(request):
    parent = request.user.parent
    reports = Report.objects.filter(Student__id__in=parent.relationships.values('Child__id'))
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
                user = User.objects.get(email=form.cleaned_data['email'])
                try:
                    parent = Parent.objects.get(user=user)
                except Parent.DoesNotExist:
                    parent = Parent.objects.create(user=user)
                student.parents.add(parent)
                try:
                    relationship = parent.relationships.get(Child=student)
                except Relationship.DoesNotExist:
                    relationship = parent.relationships.create(Parent=parent, Child=student, Relationship=form.cleaned_data['Relationship'])
                student.school.Parents.add(parent)
                message = '''
                You can now login as a parent and monitor attendance, pay fees, monitor and track performance and so much more.
                '''
                send_mail(
                    f'Linked {student} at {student.school} to your Edumetrics Parents Account',
                    message,
                    'edumetrics@sparklehandscs.com',
                    [parent.user.email]
                )
                return redirect('student-profile', student=student.id)
            except User.DoesNotExist:
                form.add_error('email', 'No Parent with such Email')
                return render(request, 'link_parent.html', {'form': form})
        else:
            print(form)
    else:
        return render(request, 'link_parent.html', context)


def parent_profile(request, parent):
    parent = Parent.objects.get(pk=parent)
    context = {
        'parent': parent
    }
    return render(request, 'parents_profile.html', context)
    

def parent_kids(request):
    return render(request, 'parent_kids.html')

def change_contact(request):
    code = generate_student_id()
    if request.method == 'POST':
        tel = request.POST['tel']
        message = client.messages.create(
            from_='+14067957780',
            body='Edumetrics Confirmation Code',
            to='+256'+tel
        )
        try:
            confirmation = TelConfirmation.objects.get(
                Tel=tel
            )
            confirmation.Code = code
        except TelConfirmation.DoesNotExist:
            TelConfirmation.objects.create(
                Tel=tel,
                Code=code
            )
        print(message.sid)
        return redirect('.')
    else:
        return render(request, 'change_contact.html')


def confirm_contact(request, confirmation):
    cf = TelConfirmation.objects.get(id=confirmation)
    if request.method == 'POST':
       pass 
    else:
        return render(request, 'change_contact.html')


