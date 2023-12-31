from django.urls import path 
from .views import teachers_dashboard, my_students, teacher_list, recruit_teacher, teacher_profile, fellow_staff, change_teacher_profile, terminate_teacher, confirm_recruit, communicate


urlpatterns = [
    path('dashboard/', teachers_dashboard, name='teacher_dashboard'),
    path('my-students/', my_students, name='my-students'),
    path('list/', teacher_list, name='teachers-list'),
    path('recruit/', recruit_teacher, name="recruit-teacher"),
    path('profile/<int:teacher>/', teacher_profile, name="teacher-profile"),
    path('fellows/', fellow_staff, name='fellow-staff'),
    path('change-profile/<int:teacher>/', change_teacher_profile, name='change-teacher-profile'),
    path('terminate/<int:teacher>/', terminate_teacher, name='terminate-teacher'),
    path('confirm-recruit/<int:user>/', confirm_recruit, name='confirm-recruit'),
    path('communicate/', communicate, name='teachers-communicate')
]
