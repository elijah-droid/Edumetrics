from django.contrib import admin
from .models import Payment, PaymentDue

admin.site.register(Payment)
admin.site.register(PaymentDue)