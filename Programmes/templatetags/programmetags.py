from django import template
from django.db.models import Sum

register = template.Library()

@register.filter
def programme_fees_total(programme):
    total = programme.Fees.filter(Compulsory=True).aggregate(total=Sum('Amount_Required'))['total']
    if not total:
        total = 0
    return total