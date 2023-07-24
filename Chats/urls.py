from django.urls import path
from .views import send_message, login

urlpatterns = [
    path('send-message/', send_message, name='send-message'),
    path('login/', login, name='chats-login')
]
