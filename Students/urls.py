from django.urls import path
from .views import generate_student_report, student_list, enroll_student


urlpatterns = [
    path('students/', student_list, name='students'),
    path('enroll-student/', enroll_student, name='enroll-student')
]