from django import template
from Reports.models import Report
from django.urls import reverse
from django.db.models import Sum
from FeesManagement.models import Payment


register = template.Library()

@register.filter
def fees_balance(student):
    amt = student.school.Dues.filter(Compulsory=True).aggregate(total=Sum('Amount_Required'))['total']
    paid = Payment.objects.filter(Due__Compulsory=True).aggregate(total=Sum('Amount'))['total']
    return amt - paid

@register.filter
def due_balance(student, due):
    paid = due.Payments.filter(Student=student).aggregate(total=Sum('Amount'))['total']
    balance = due.Amount_Required - paid
    return balance


@register.filter
def amount_paid(due):
    paid = due.Payments.aggregate(total=Sum('Amount'))['total']
    return paid
