from django.urls import path
from .views import school_profile


urlpatterns = [
    path('profile/<int:school>/', school_profile, name='school-profile')
]