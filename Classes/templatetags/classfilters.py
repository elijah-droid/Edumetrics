from django import template
from Attendance.models import Attendance
from django.utils.timezone import now

register = template.Library()

@register.filter
def attendance(clas, request):
    att = Attendance.objects.get(Class=clas, School=request.user.schooladministrator.current_school, Date=now().date)
    return att.Students
