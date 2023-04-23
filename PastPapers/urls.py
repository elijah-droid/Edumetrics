from django.urls import path
from .views import parent_view_pastpapers


urlpatterns = [
    path('parents-view/', parent_view_pastpapers, name="parent-pastpapers"),
]