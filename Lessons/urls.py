from django.urls import path
from .views import lessons, add_new


urlpatterns = [
    path('today/', lessons, name='lessons'),
    path('new/', add_new, name='new-lesson')
]