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
    try:
        report = Report.objects.get(Examination=result.Paper.Examination, Student=student)
    except ObjectDoesNotExist:
        report = Report.objects.create(Examination=result.Paper.Examination, Student=student)
    if report not in paper.Examination.School.Reports.all():
        paper.Examination.School.Reports.add(report)
    if result not in report.Results.all():
        report.Results.add(result)
    return result.Score