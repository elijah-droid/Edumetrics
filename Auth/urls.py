from django.urls import path
from .views import parents_login, admin_login, student_login, teacher_login, logout_view, set_school_session, signup, user_login


urlpatterns = [
    path('login-parent/', parents_login, name='login-parent'),
    path('admin-login/', admin_login, name='admin-login'),
    path('login-student/', student_login, name='login-student'),
    path('login-teacher/', teacher_login, name='login-teacher'),
    path('set-school-session/<int:school>/', set_school_session, name='set-school-session'),
    path('user-login/', user_login, name='user-login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout')
]
