from django.urls import path
from .views import parent_requirements, add_programme_requirement

urlpatterns = [
    path('parents/', parent_requirements, name='parent-requirements'),
    path('add/<int:programme>/', add_programme_requirement, name="add-programme-requirement")
]