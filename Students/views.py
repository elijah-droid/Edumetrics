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

def generate_student_id():
    # Generate a 4-letter random string
    letters = string.ascii_uppercase
    random_letters = ''.join(random.choice(letters) for i in range(4))
    
    # Generate a 4-digit random number
    random_number = str(random.randint(1000, 9999))
    
    # Combine the two to form a student ID
    student_id = random_letters + random_number
    
    return student_id


def generate_student_report(request):
    students = Student.objects.all()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="student_report.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Set up the PDF document
    p.setTitle("Student Report")
    p.setFont("Helvetica-Bold", 16)
    p.drawCentredString(300, 750, "Student Report")
    p.setFont("Helvetica", 12)

    # Generate the content for the PDF
    y = 700
    p.drawString(50, y, f"Names")
    p.drawString(150, y, f"Male")
    p.drawString(250, y, f"{student.date_of_birth}")
    p.drawString(350, y, f"1")
    y -= 20
    for student in students:
        p.drawString(50, y, f"{student.first_name} {student.last_name}")
        p.drawString(150, y, f"Male")
        p.drawString(250, y, f"{student.date_of_birth}")
        p.drawString(350, y, f"1")
        y -= 20

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
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
            student = form.save()
            student.school = request.user.schooladministrator.current_school
            request.user.schooladministrator.current_school.students.add(student)
            cls = form.cleaned_data['Class']
            cls.Students.add(student)
            subjects = form.cleaned_data['Subjects']
            student.Subjects.set(subjects)
            student.Class = cls
            student.save()
            for subject in student.Subjects.all():
                subject.Students.add(student)
            messages.success(request, f'Student {student.first_name} {student.last_name} has been enrolled successfully.')
            return redirect('students')
    else:
        form = StudentForm(initial={'student_id': generate_student_id()})
        form.fields['Subjects'].queryset = request.user.schooladministrator.current_school.Subjects.all()
        form.fields['Class'].queryset = request.user.schooladministrator.current_school.classes.all()
    return render(request, 'enroll_student.html', {'form': form})




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
    classes = Class.objects.filter(Students__school__id=request.user.schooladministrator.current_school.id)
    return render(request, 'student_list.html', {'classes': classes})

