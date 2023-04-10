from django.contrib import admin
from .models import SchoolAdministrator, Adminship


class AdminshipAdmin(admin.ModelAdmin):
    list_filter = ('Admin',)
    list_display = ('Admin', 'School', 'super_admin')

admin.site.register(SchoolAdministrator)
admin.site.register(Adminship, AdminshipAdmin)