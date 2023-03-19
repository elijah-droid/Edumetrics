from django.contrib import admin
from django.urls import path, include
from .views import index, user_dashboard
from django.contrib import admin
from allauth.account.views import LoginView

admin.site.site_header = "Edumetrics Inc"

urlpatterns = [
    path('', index, name='index'),
    path('user/dashboard/', user_dashboard, name="user-dashboard"),
    path('auth/', include('Auth.urls')),
    path('school-admin/', include('SchoolAdministrators.urls')),
    path('', include('Students.urls')),
    path('teachers/', include('Teachers.urls')),
    path('parents/', include('Parents.urls')),
    path('reports/', include('Reports.urls')),
    path('examinations/', include('Examinations.urls')),
    path('events/', include('Events.urls')),
    path('classes/', include('Classes.urls')),
    path('attendance/', include('Attendance.urls')),
    path('grading/', include('Grading.urls')),
    path('subscriptions/', include('Subscriptions.urls')),
    path('subjects/', include('Subjects.urls')),
    path('circulars/', include('Circulars.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]
