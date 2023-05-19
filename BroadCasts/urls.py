from django.urls import path
from .views import to_broadcast

urlpatterns = [
    path('to-do/', to_broadcast, name='to-broadcast')
]