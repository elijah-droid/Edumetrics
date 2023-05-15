from django.urls import path 
from .views import examination_list, schedule_exam, view_exam_reports, assessments, delete_examination, exam_papers, schedule_paper, paper_results


urlpatterns = [
    path('list/', examination_list, name='examinations'),
    path('schedule/', schedule_exam, name='schedule-exam'),
    path('reports/<int:exam>/', view_exam_reports, name='exam-reports'),
    path('assessments/<int:exam>/', assessments, name='assessments'),
    path('delete/<int:exam>/', delete_examination, name='delete-exam'),
    path('papers/<int:exam>/', exam_papers, name='exam-papers'),
    path('schedule-paper/<int:exam>/', schedule_paper, name='schedule-paper'),
    path('paper-results/<int:paper>/', paper_results, name='paper-results')
]
