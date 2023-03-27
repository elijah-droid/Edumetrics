from django import template
from Reports.models import Score
from django.urls import reverse
from django.db.models import Avg

register = template.Library()

@register.simple_tag
def average_score(student, subject):
    scores = Score.objects.filter(Report__Student=student, Subject=subject)
    average = scores.aggregate(Avg('Score'))['Score__avg']
    try:
        return int(average)
    except:
        return 0
