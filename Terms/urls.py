from django.urls import path 
from .views import terms

urlpatterns = [
    path('configured/', terms, name="terms"),
]