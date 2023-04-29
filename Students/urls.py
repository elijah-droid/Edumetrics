from django.urls import path
from .views import student_list, enroll_student, student_profile, child_info, download_students_info, change_student, old_students, terminate_student, old_students


urlpatterns = [
    path('list/', student_list, name='students'),
    path('enroll/<int:level>/', enroll_student, name='enroll-student'),
    path('profile/<int:student>/', student_profile, name="student-profile"),
    path('child/info/<int:child>/', child_info, name="child-info"),
    path('download-info/', download_students_info, name="download-students-info"),
    path('change/<int:student>/', change_student, name="change-student"),
    path('old/', old_students, name="old-students"),
    path('terminate/<int:student>/', terminate_student, name='terminate-student'),
]