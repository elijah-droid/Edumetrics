from django.urls import path
from .views import classes, add_class


urlpatterns = [
    path('list/', classes, name='classes'),
    path('add/', add_class, name='add-class')
]