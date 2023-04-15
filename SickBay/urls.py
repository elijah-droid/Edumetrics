from django.urls import path
from .views import admissions, admit


urlpatterns = [
    path('admissions/', admissions, name='admissions'),
    path('admit/', admit, name='admit')
]