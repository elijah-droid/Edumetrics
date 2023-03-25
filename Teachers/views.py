from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Teacher
from .forms import TeachersForm
from Lessons.models import Lesson
from django.utils.timezone import now

@login_required
def teachers_dashboard(request):
    day = now().strftime("%A")
    lessons = Lesson.objects.filter(Teacher__user=request.user, Day=day)
    context = {
        'lessons': lessons
    }
    return render(request, 'teachers_dashboard.html', context)


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
    teachers = Teacher.objects.all()
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
    content = {
        'form': form
    }
    return render(request, 'recruit_teacher.html', content)