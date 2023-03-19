from django.urls import path 
from .views import circulars


urlpatterns = [
    path('list/', circulars, name='circulars'),
]