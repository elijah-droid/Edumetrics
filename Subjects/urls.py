from django.urls import path 
from .views import subject_list, add_subject, delete_subject


urlpatterns = [
    path('list/', subject_list, name='subjects'),
    path('add/', add_subject, name='add-subject'),
    path('delete/<int:subject_id>/', delete_subject, name='delete-subject')
]