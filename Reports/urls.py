from django.urls import path 
from .views import view_report, reports, batch_reports, edit_report, student_reports, create_report


urlpatterns = [
    path('report/', view_report, name='view-report'),
    path('list/', reports, name='reports'),
    path('create-batch/', batch_reports, name='create-batch'),
    path('edit/<int:report>/', edit_report, name='edit-report'),
    path('<int:student>/', student_reports, name="student-reports"),
    path('create/<int:student>/<int:examination>/', create_report, name='create-report')
]
