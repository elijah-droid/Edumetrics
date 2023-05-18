from django.urls import path 
from .views import subject_list, add_subject, delete_subject, combinations, add_combination, edit_subject


urlpatterns = [
    path('list/', subject_list, name='subjects'),
    path('add/', add_subject, name='add-subject'),
    path('edit/<int:subject_id>/', edit_subject, name='edit-subject'),
    path('delete/<int:subject_id>/', delete_subject, name='delete-subject'),
    path('combinations/', combinations, name="combinations"),
    path('add-combinaion/', add_combination, name="add-combination")
]