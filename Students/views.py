from django.shortcuts import render, redirect
from django.http import HttpResponse
from Students.models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
import random
from Classes.models import Class
import string
from Enrollments.models import Enrollment
import docx
from django.http import FileResponse
import io
from docx.enum.text import WD_ALIGN_PARAGRAPH
from FeesManagement.templatetags.fees_tags import fees_balance


def generate_student_id():
    # Generate a 4-letter random string
    letters = string.ascii_uppercase
    random_letters = ''.join(random.choice(letters) for i in range(4))
    
    # Generate a 4-digit random number
    random_number = str(random.randint(1000, 9999))
    
    # Combine the two to form a student ID
    student_id = random_letters + random_number
    
    return student_id


def download_students_info(request):
    doc = docx.Document()
    doc.add_heading(f'{request.user.schooladministrator.current_school} Students Info', level=1).alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph()
    table = doc.add_table(rows=request.user.schooladministrator.current_school.students.count()+1, cols=6)
    table.cell(0, 0).text = 'First Name'
    table.cell(0, 1).text = 'Last_Name'
    table.cell(0, 2).text = 'Class'
    table.cell(0, 3).text = 'Student Id'
    table.cell(0, 4).text = 'Date Enrolled'
    table.cell(0, 5).text = 'Fees Balance'
    row = 1
    for student in request.user.schooladministrator.current_school.students.all():
        table.cell(row, 0).text = student.first_name
        table.cell(row, 1).text = student.last_name
        table.cell(row, 2).text = student.Class.Name
        table.cell(row, 3).text = student.student_id
        table.cell(row, 4).text = str(student.active_enrollment.Date)
        table.cell(row, 5).text = f'{fees_balance(student)} UGX'
        row += 1

    document_io = io.BytesIO()
    doc.save(document_io)
    document_io.seek(0)
    response = FileResponse(document_io, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename="{request.user.schooladministrator.current_school}_students_info.docx"'
    return response


def student_dashboard(request):
    # Get the logged-in student user
    student = request.user.student

    # Get the student's upcoming exams
    upcoming_exams = student.exam_set.filter(status='scheduled')

    # Get the student's recent exam results
    recent_results = student.examresult_set.order_by('-date').all()[:10]

    context = {
        'student': student,
        'upcoming_exams': upcoming_exams,
        'recent_results': recent_results,
    }

    return render(request, 'student_dashboard.html', context)


@login_required
def enroll_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.school = request.user.schooladministrator.current_school
            student.user = User.objects.create(username=form.cleaned_data['student_id'])
            student.save()
            request.user.schooladministrator.current_school.students.add(student)
            cls = form.cleaned_data['Class']
            cls.Students.add(student)
            subjects = form.cleaned_data['Subjects']
            student.Subjects.set(subjects)
            student.Class = cls
            student.save()
            for subject in student.Subjects.all():
                subject.Students.add(student)
            enrollment = Enrollment.objects.create(School=request.user.schooladministrator.current_school, Student=student, Programme=student.Programme, By=request.user.schooladministrator)
            student.active_enrollment = enrollment
            student.save()
            student.school.Enrollments.add(enrollment)
            messages.success(request, f'Student {student.first_name} {student.last_name} has been enrolled successfully.')
            return redirect('students')
    else:
        form = StudentForm(initial={'student_id': generate_student_id()})
        form.fields['Subjects'].queryset = request.user.schooladministrator.current_school.Subjects.all()
        form.fields['Class'].queryset = request.user.schooladministrator.current_school.classes.all()
    return render(request, 'enroll_student.html', {'form': form})


def change_student(request, student):
    student = request.user.schooladministrator.current_school.students.get(pk=student)
    form = StudentForm(instance=student)
    form.fields['Subjects'].queryset = request.user.schooladministrator.current_school.Subjects.all()
    form.fields['Class'].queryset = request.user.schooladministrator.current_school.classes.all()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Student {student.first_name} {student.last_name} info was changed successfully.')
            return redirect('students')
        else:
            print(form)
    else:
        return render(request, 'change_student.html', context)


def  import_student(request):
    return render(request, 'import_student.html')


def child_info(request, child):
    child = Student.objects.get(pk=child)
    context = {
        'child': child
    }
    return render(request, 'child_info.html', context)


def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.school = request.user.teacher.school
            student.save()
            messages.success(request, 'Student updated successfully')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form, 'student': student})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully')
        return redirect('student_list')
    return render(request, 'delete_student.html', {'student': student})

def student_list(request):
    students = request.user.schooladministrator.current_school.students.all().order_by('active_enrollment__Date').reverse()
    context = {
        'students': students
    }
    return render(request, 'student_list.html', context)


def student_profile(request, student):
    student = request.user.schooladministrator.current_school.students.get(pk=student)
    context = {
        'student': student
    }
    return render(request, 'student_profile.html', context)