from django.contrib import admin
from .models import PasswordReset, EmailConfirmation


admin.site.register(PasswordReset)
admin.site.register(EmailConfirmation)
