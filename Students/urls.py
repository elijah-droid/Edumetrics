from django.urls import path
from .views import generate_student_report, student_list, enroll_student, student_profile


urlpatterns = [
    path('list/', student_list, name='students'),
    path('enroll/', enroll_student, name='enroll-student'),
    path('profile/<int:student>/', student_profile, name="student-profile")
]