from django import template
from Reports.models import Report
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.filter
def paper_result(paper, student):
    try:
        result = paper.Results.get(Student=student)
    except ObjectDoesNotExist:
        result = paper.Results.create(Paper=paper, Student=student)
    return result.Score