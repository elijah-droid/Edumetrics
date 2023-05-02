from django.contrib import admin
from .models import School


class SchoolAdmin(admin.ModelAdmin):
    fields = ('name', 'motto', 'badge', 'address', 'city', 'state', 'zip_code')

admin.site.register(School, SchoolAdmin)