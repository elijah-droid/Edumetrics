from django.urls import path
from .views import send_message

urlpatterns = [
    path('send-message/', send_message, name='send-message'),
    
]
