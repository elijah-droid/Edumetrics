from django.urls import path 
from .views import parent_dashboard, parents_list


urlpatterns = [
    path('dashboard/', parent_dashboard, name='parent_dashboard'),
    path('list/', parents_list, name='parents-list')
]
