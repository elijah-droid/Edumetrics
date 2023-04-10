from django.urls import path
from .views import student_list, enroll_student, student_profile, child_info, download_students_info


urlpatterns = [
    path('list/', student_list, name='students'),
    path('enroll/', enroll_student, name='enroll-student'),
    path('profile/<int:student>/', student_profile, name="student-profile"),
    path('child/info/<int:child>/', child_info, name="child-info"),
    path('download-info/', download_students_info, name="download-students-info")
]