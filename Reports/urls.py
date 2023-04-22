from django.urls import path 
from .views import view_report, reports, edit_report, student_reports, create_report, publish_batch, child_reports


urlpatterns = [
    path('report/', view_report, name='view-report'),
    path('list/', reports, name='reports'),
    path('edit/<int:report>/', edit_report, name='edit-report'),
    path('<int:student>/', student_reports, name="student-reports"),
    path('create/<int:student>/<int:examination>/', create_report, name='create-report'),
    path('publish-batch/', publish_batch, name='publish-batch'),
    path('children/', child_reports, name="child-reports")
]
