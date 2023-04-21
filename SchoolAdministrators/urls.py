from django.urls import path 
from .views import school_admin_dashboard, school_administrators, register_schooladmin, change_permissions, teacher_administrators


urlpatterns = [
    path('dashboard/', school_admin_dashboard, name='admin_dashboard'),
    path('list/', school_administrators, name='school-administrators'),
    path('register/', register_schooladmin, name="register-schooladmin"),
    path('change-permissions/<int:admin>/', change_permissions, name='change-permissions'),
    path('teacher-admins/', teacher_administrators, name='teacher-admins')
]