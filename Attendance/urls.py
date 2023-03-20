from django.urls import path 
from .views import attendance, add_attenance


urlpatterns = [
    path('records/', attendance, name='attendance'),
    path('add/', add_attenance, name="add-attendance")
]
