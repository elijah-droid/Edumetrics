from django.urls import path 
from .views import school_admin_dashboard, school_administrators, register_schooladmin


urlpatterns = [
    path('dashboard/', school_admin_dashboard, name='admin_dashboard'),
    path('list/', school_administrators, name='school-administrators'),
    path('register/', register_schooladmin, name="register-schooladmin")
]