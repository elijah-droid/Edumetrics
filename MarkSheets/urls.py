from django.urls import path
from .views import marksheets, marksheet_tallies, create_marksheet, add_score, exam_marksheets


urlpatterns = [
    path('List/', marksheets, name='mark-sheets'),
    path('scores/<int:marksheet>/', marksheet_tallies, name='marksheet-tallies'),
    path('create/', create_marksheet, name='create-marksheet'),
    path('add-score/<int:marksheet>/', add_score, name='marksheet-add-score'),
    path('exam/<int:exam>/', exam_marksheets, name='exam-marksheets')
]