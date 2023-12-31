from django.urls import path
from .views import parents_login, admin_login, student_login, teacher_login, logout_view, set_school_session, signup, user_login, change_password, confirm_email, forgot_password, reset_password, teacher_switch_profile, signup_details


urlpatterns = [
    path('login-parent/', parents_login, name='login-parent'),
    path('admin-login/', admin_login, name='admin-login'),
    path('login-student/', student_login, name='login-student'),
    path('login-teacher/', teacher_login, name='login-teacher'),
    path('set-school-session/<int:school>/', set_school_session, name='set-school-session'),
    path('user-login/', user_login, name='user-login'),
    path('change-password/', change_password, name='change-password'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('confirm-email/<int:user>/', confirm_email, name='confirm-email'),
    path('forgot-password/', forgot_password, name='forgot-password'),
    path('reset-password/<int:reset>/', reset_password, name='reset-password'),
    path('switch-teachers-profile/<int:profile>/', teacher_switch_profile, name='switch-profile'),
    path('signup-details/<int:confirmation>/', signup_details, name='signup-details')
]
