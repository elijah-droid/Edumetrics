from django.shortcuts import render, redirect
from .forms import LessonForm


def lessons(request):
    return render(request, 'lessons.html')

def add_new(request):
    form = LessonForm()
    form.fields['Class'].queryset = request.user.schooladministrator.current_school.classes.all()
    form.fields['Subject'].queryset = request.user.schooladministrator.current_school.Subjects.all()
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
            return redirect('lessons')
    else:
        return render(request, 'new_lesson.html', context)


