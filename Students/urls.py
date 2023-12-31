from django.urls import path
from .views import student_list, enroll_student, student_profile, child_info, download_students_info, change_student, old_students, terminate_student, old_students, select_student_class, search_student, get_qr, setup_account, student_dashboard, generate_idcard


urlpatterns = [
    path('list/', student_list, name='students'),
    path('enroll/<int:clas>/', enroll_student, name='enroll-student'),
    path('profile/<int:student>/', student_profile, name="student-profile"),
    path('child/info/<int:child>/', child_info, name="child-info"),
    path('download-info/', download_students_info, name="download-students-info"),
    path('change/<int:student>/', change_student, name="change-student"),
    path('old/', old_students, name="old-students"),
    path('terminate/<int:student>/', terminate_student, name='terminate-student'),
    path('select-class/', select_student_class, name='select-student-class'),
    path('search/', search_student, name='search-student'),
    path('get-qr-code/<int:student>/', get_qr, name='get-qr'),
    path('setup-account/<int:student>/', setup_account, name='setup-account'),
    path('dashboard/', student_dashboard, name='students-dashboard'),
    path('generate-id/<int:student>/', generate_idcard, name='generate-idcard')
]