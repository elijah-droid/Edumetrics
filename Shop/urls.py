from django.urls import path
from .views import products


urlpatterns = [
    path('products/<str:sector>/', products, name='products'),
]