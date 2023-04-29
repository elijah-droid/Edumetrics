from django import template
from EducationHistory.models import EducationHistory

register = template.Library()

@register.filter
def education_history(student, school):
    history = EducationHistory.objects.get(Student=student, School=school)
    return history
