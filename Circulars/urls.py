from django.urls import path 
from .views import circulars, add_circular


urlpatterns = [
    path('list/', circulars, name='circulars'),
    path('add/', add_circular, name='add-circular')
]