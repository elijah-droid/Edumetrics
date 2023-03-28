from django import template
from django.db.models import Avg
from Reports.models import Report, Score
from django.urls import reverse

register = template.Library()

@register.filter
def profile(teacher, school):
    profile = teacher.work_profile.get(School=school)
    return profile


@register.simple_tag
def teacher_score(teacher, subject, school):
    profile = teacher.work_profile.get(School=school)
    scores = Score.objects.filter(Subject=subject)
    print(scores)
    figure = scores.aggregate(score=Avg('Score'))['score']
    try:
        return int(figure)
    except:
        return 0