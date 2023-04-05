from django import template
from Reports.models import Report
from django.urls import reverse
from django.db.models import Sum


register = template.Library()

@register.filter
def fees_balance(student):
    amt = student.school.Dues.aggregate(total=Sum('Amount_Required'))['total']
    return amt
