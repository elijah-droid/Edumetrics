from django.shortcuts import render
from .forms import LessonForm

def lessons(request):
    return render(request, 'lessons.html')

def add_new(request):
    form = LessonForm()
    context = {
        'form': form
    }
    return render(request, 'new_lesson.html', context)