from django.contrib import admin
from .models import Book, LendOut


admin.site.register(Book)
admin.site.register(LendOut)