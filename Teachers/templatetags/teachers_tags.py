from django import template
from django.db.models import Avg
from Reports.models import Report, Score
from django.urls import reverse
from Lessons.models import Lesson
from django.utils.timezone import now

register = template.Library()

@register.filter
def profile(teacher, school):
    profile = teacher.work_profile.get(School=school)
    return profile


@register.simple_tag
def teacher_score(teacher, subject, school):
    profile = teacher.work_profile.get(School=school)
    scores = Score.objects.filter(Subject=subject, Report__Student__Class__in=profile.Classes.all(), Report__Student__school=profile.School)
    print(scores)
    figure = scores.aggregate(score=Avg('Score'))['score']
    try:
        return int(figure)
    except:
        return 0

@register.filter
def students(teacher, school):
    profile = teacher.work_profile.get(School=school)
    students = school.students.filter(Class__in=profile.Classes.all(), school=profile.School, Subjects__in=profile.Subjects.all()).distinct()
    return students


@register.filter
def lessons(teacher, school):
    day = now().strftime("%A")
    lessons = Lesson.objects.filter(Teacher=teacher, School=school, Day=day)
    return lessons