from django.urls import path
from .views import enrollments

urlpatterns = [
    path('list/', enrollments, name="enrollments")
]