from django.urls import path 
from.views import messages

urlpatterns = [
    path('inbox/',messages, name='messages'),
]