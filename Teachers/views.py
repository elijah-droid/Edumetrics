from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Teacher
from .forms import TeachersForm
from Lessons.models import Lesson
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist


@login_required
def teachers_dashboard(request):
    return render(request, 'teachers_dashboard.html')


@login_required
def my_students(request):
    teacher = request.user.teacher
    students = teacher.current_school.students.filter(Class=teacher.current_class, stream=teacher.current_stream)
    teacher = Teacher.objects.get(user=request.user)
    # Get all the students taught by the current user
    students = Student.objects.filter(teacher=teacher)
    context = {'students': students}
    return render(request, 'my_students.html', context)

@login_required
def class_teacher_dashboard(request):
    # Get the currently logged in user (assumed to be the class teacher)
    user = request.user
    
    # Get the class that the class teacher is responsible for
    try:
        class_teacher = user.class_teacher
        class_ = class_teacher.class_
    except:
        class_teacher = None
        class_ = None
    
    # Get all the students in the class
    students = Student.objects.filter(class_=class_)
    
    # Get the latest exam results for each student in the class
    latest_results = []
    for student in students:
        latest_result = ExamResult.objects.filter(student=student).order_by('-exam__date').first()
        if latest_result:
            latest_results.append(latest_result)
    
    # Render the template with the necessary data
    return render(request, 'class_teacher_dashboard.html', {
        'class_teacher': class_teacher,
        'class': class_,
        'students': students,
        'latest_results': latest_results
    })


def teacher_list(request):
    teachers = Teacher.objects.all().order_by('id')
    paginator = Paginator(teachers, 10)
    page = request.GET.get('page')
    teachers = paginator.get_page(page)
    return render(request, 'teacher_list.html', {'teachers': teachers})

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'teacher_detail.html', {'teacher': teacher})

def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Teacher created successfully')
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'teacher_form.html', {'form': form})

def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, 'Teacher updated successfully')
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'teacher_form.html', {'form': form})

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        messages.success(request, 'Teacher deleted successfully')
        return redirect('teacher_list')
    return render(request, 'teacher_confirm_delete.html', {'teacher': teacher})


def recruit_teacher(request):
    form = TeachersForm()
    del form.fields['Classes']
    del form.fields['Subjects']
    content = {
        'form': form
    } 
    if request.method == 'POST':
        form = TeachersForm(request.POST)
        del form.fields['Classes']
        del form.fields['Subjects']
        if form.is_valid():
            try:
                user = User.objects.get(email=form.cleaned_data['email'])
                try:
                    request.user.schooladministrator.current_school.Teachers.get(user__email=form.cleaned_data['email'])
                    messages.success(request, 'User is already a teacher in this school.')
                    return redirect('.')
                except ObjectDoesNotExist:
                    return redirect('confirm-recruit', user=user.id)
            except User.DoesNotExist:
                messages.success(request, 'Unregistered Email')
                return redirect('.')

    else:
        return render(request, 'recruit_teacher.html', content)


def teacher_profile(request, teacher):
    teacher = Teacher.objects.get(pk=teacher)
    context = {
        'teacher': teacher
    }
    return render(request, 'teacher_profile.html', context)


def fellow_staff(request):
    return render(request, 'fellow_staff.html')


def change_teacher_profile(request, teacher):
    teacher = Teacher.objects.get(id=teacher)
    profile = teacher.work_profile.get(School=request.user.schooladministrator.current_school)
    form = TeachersForm(instance=profile)
    del form.fields['email']
    form.fields['Classes'].queryset = request.user.schooladministrator.current_school.classes.all()
    form.fields['Subjects'].queryset = request.user.schooladministrator.current_school.Subjects.all()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = TeachersForm(request.POST, instance=profile)
        del form.fields['email']
        if form.is_valid():
            form.save()
            return redirect('teachers-list')
    else:
        return render(request, 'change_teacher_profile.html', context)


def terminate_teacher(request, teacher):
    teacher = request.user.schooladministrator.current_school.Teachers.get(id=teacher)
    profile = teacher.work_profile.get(School=request.user.schooladministrator.current_school)
    context = {
        'teacher': teacher
    }
    if request.method == "POST":
        data = request.POST
        answer = data['answer']
        if answer == 'yes':
            profile.delete()
            message = f'''
            Dear {teacher}, you have been terminated from {request.user.schooladministrator.current_school}
            '''
            send_mail(
                'TERMINATION NOTICE',
                message,
                "Edumetrics <info@edu-metrics.com>",
                [teacher.user.email]
            )
            messages.success(request, "Teacher has been terminated successfully.")
            return redirect("teachers-list")
        else:
            messages.success(request, "operation cancelled")
            return redirect("teachers-list")
    else: 
        return render(request, 'terminate_teacher.html', context)


def confirm_recruit(request, user):
    user = User.objects.get(id=user)
    try:
        teacher = Teacher.objects.get(user=user)
    except Teacher.DoesNotExist:
        teacher = Teacher.objects.create(
            user=user
        )
    form = TeachersForm()
    del form.fields['email']
    form.fields['Classes'].queryset = request.user.schooladministrator.current_school.classes.all()
    form.fields['Subjects'].queryset = request.user.schooladministrator.current_school.Subjects.all()
    context = {
        'teacher': user,
        'form': form
    }
    if request.method == 'POST':
        form = TeachersForm(request.POST)
        del form.fields['email']
        if form.is_valid():
            if request.POST['answer'] == 'yes':
                profile = form.save(commit=False)
                profile.School = request.user.schooladministrator.current_school
                profile.Teacher = teacher
                profile.save()
                teacher.work_profile.add(profile)
                profile.Classes.set(form.cleaned_data['Classes'])
                profile.Subjects.set(form.cleaned_data['Subjects'])
                message = f'''
                    You have been recruited as a teacher at {request.user.schooladministrator.current_school},
                    Subjects are {', '.join(str(s) for s in profile.Subjects.all())} and Classes are {', '.join(str(c) for c in profile.Classes.all())}
                '''
                send_mail(
                    'You have been recruited',
                    message,
                    'Edumetrics <info@edu-metrics.com>',
                    [teacher.user.email]
                )
                messages.success(request, f'Teacher recruited successfully.')
                return redirect('teachers-list')
            else:
                messages.success(request, 'Operation Cancelled')
                return redirect('teachers-list')
    else:
        return render(request, 'confirm_recruit.html', context)


    