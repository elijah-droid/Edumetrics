from django import template
from Reports.models import Report
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()

@register.simple_tag
def get_score(exam, student, subject):
    try:
        report = Report.objects.get(Student=student, Examination=exam)
        score = report.Scores.get(Subject=subject)
        return score.Score
    except ObjectDoesNotExist:
        return "XXX"


@register.simple_tag
def edit_report(exam, student):
    try:
        report = Report.objects.get(Student=student, Examination=exam)
        url = reverse('edit-report', args=[report.id])
        return url
    except Report.DoesNotExist:
        return reverse('create-report', args=[student.id, exam.id])