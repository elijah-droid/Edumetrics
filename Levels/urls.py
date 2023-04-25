from django.urls import path
from .views import levels, add_level


urlpatterns = [
    path('list/', levels, name='levels'),
    path('add/', add_level, name='add-level')
]