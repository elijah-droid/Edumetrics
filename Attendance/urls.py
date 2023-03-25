from django.urls import path 
from .views import attendance, add_attenance, roll_call


urlpatterns = [
    path('records/', attendance, name='attendance'),
    path('add/', add_attenance, name="add-attendance"),
    path('roll_call/<int:lesson>/', roll_call, name="roll-call")
]
