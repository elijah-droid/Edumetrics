from django.urls import path 
from .views import parent_dashboard, parents_list, link_parent, parent_profile, parent_kids, change_contact


urlpatterns = [
    path('dashboard/', parent_dashboard, name='parent_dashboard'),
    path('list/', parents_list, name='parents-list'),
    path('link/<int:student>/', link_parent, name='link-parent'),
    path('profile/<int:parent>/', parent_profile, name="parent-profile"),
    path('kids/', parent_kids, name='kids'),
    path('change-contact/', change_contact, name="change-contact")
]
