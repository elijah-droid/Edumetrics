from django.urls import path
from .views import lessons, add_new, teacher_lessons


urlpatterns = [
    path('today/', lessons, name='lessons'),
    path('new/', add_new, name='new-lesson'),
    path('teachers/', teacher_lessons, name='teacher-lessons')
]