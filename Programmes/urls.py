from django.urls import path
from .views import programmes, add_programme

urlpatterns = [
    path('list/', programmes, name='programmes'),
    path('new/', add_programme, name='add-programme')
]