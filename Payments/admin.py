from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('account', 'amount', 'wallet', 'Status')

admin.site.register(Payment, PaymentAdmin)