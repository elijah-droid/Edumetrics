from django.urls import path 
from .views import parent_dashboard, parents_list, link_parent


urlpatterns = [
    path('dashboard/', parent_dashboard, name='parent_dashboard'),
    path('list/', parents_list, name='parents-list'),
    path('link/<int:student>/', link_parent, name='link-parent')
]
