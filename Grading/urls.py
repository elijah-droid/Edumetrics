from django.urls import path
from .views import grades, divisions, add_grade, add_division

urlpatterns = [
    path('grades/', grades, name='grades'),
    path('divisions/', divisions, name='divisions'),
    path('new/', add_grade, name='add-grade'),
    path('new-division/', add_division, name='add-division'),
]