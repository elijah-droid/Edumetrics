from django import template
from Attendance.models import Attendance
from django.utils.timezone import now

register = template.Library()

@register.filter
def attendance(clas, request):
    try:
        att = Attendance.objects.get(Class=clas, School=request.user.schooladministrator.current_school, Date=now())
        return att.Students
    except Attendance.DoesNotExist:
        return 0


