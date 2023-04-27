from django.urls import path
from .views import parent_requirements, add_programme_requirement, child_requirements, delete_requirement

urlpatterns = [
    path('parents/', parent_requirements, name='parent-requirements'),
    path('add/<int:programme>/', add_programme_requirement, name="add-programme-requirement"),
    path('child/<int:child>/', child_requirements, name='child-requirements'),
    path('delete/<int:requirement>/', delete_requirement, name='delete-requirement')
]