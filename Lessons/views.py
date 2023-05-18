from django.shortcuts import render, redirect
from .forms import LessonForm
from django.core.mail import send_mail


def lessons(request):
    return render(request, 'lessons.html')

def add_new(request):
    form = LessonForm()
    form.fields['Class'].queryset = request.user.schooladministrator.current_school.classes.all()
    form.fields['Subject'].queryset = request.user.schooladministrator.current_school.Subjects.all()
    form.fields['Teacher'].queryset = request.user.schooladministrator.current_school.Teachers.all()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.School = request.user.schooladministrator.current_school
            lesson.save() 
            lesson.Class.Lessons.add(lesson)
            request.user.schooladministrator.current_school.Lessons.add(lesson)
            lesson.Teacher.Lessons.add(lesson)
            message = f'''
                You will be teaching {lesson.Subject} in {lesson.Class} class every {lesson.Day}
                From {lesson.From} to {lesson.To}
            '''
            send_mail(
                f'{request.user.schooladministrator.current_school} TimeTable Tweak',
                message,
                'edumetrics@sparklehandscs.com',
                [lesson.Teacher.user.email]
            )
            return redirect('lessons')
    else:
        return render(request, 'new_lesson.html', context)


def teacher_lessons(request):
    return render(request, 'teacher_lessons.html')