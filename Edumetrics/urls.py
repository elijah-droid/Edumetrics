from django.contrib import admin
from django.urls import path, include
from .views import index, user_dashboard, contact_us, about_us
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "Edumetrics Inc"

urlpatterns = [
    path('', index, name='index'),
    path('user/dashboard/', user_dashboard, name="user-dashboard"),
    path('auth/', include('Auth.urls')),
    path('school-admin/', include('SchoolAdministrators.urls')),
    path('students/', include('Students.urls')),
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
    path('lessons/', include('Lessons.urls')),
    path('tallies/', include('Tallies.urls')),
    path('Dues/', include('FeesManagement.urls')),
    path('contact/us/', contact_us, name='contact-us'),
    path('about/us/', about_us, name="about"),
    path('terms/', include('Terms.urls')),
    path('messages/', include('Messages.urls')),
    path('enrollments/', include('Enrollments.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'Edumetrics.views.handler404'
handler500 = 'Edumetrics.views.handler500'
