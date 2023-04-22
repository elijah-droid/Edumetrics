from django import template
from django.db.models import Sum

register = template.Library()

@register.filter
def book_lendouts(book):
    lendouts = book.Lend_Outs.filter(Returned=False).aggregate(total=Sum('Number'))['total']
    if lendouts:
        return lendouts
    else:
        return 0