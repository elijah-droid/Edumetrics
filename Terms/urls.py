from django.urls import path 
from .views import terms, new_term, switch_term, change_term_dates

urlpatterns = [
    path('configured/', terms, name="terms"),
    path('configure/', new_term, name="new-term"),
    path('switch/<int:term>/', switch_term, name="switch-term"),
    path('change-dates/<int:term>/', change_term_dates, name='change-term-dates')
]