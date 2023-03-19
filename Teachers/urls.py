from django.urls import path 
from .views import teachers_dashboard, my_students, teacher_list, recruit_teacher


urlpatterns = [
    path('dashboard/', teachers_dashboard, name='teacher_dashboard'),
    path('my-students/', my_students, name='my-students'),
    path('list/', teacher_list, name='teachers-list'),
    path('recruit/', recruit_teacher, name="recruit-teacher")
]
