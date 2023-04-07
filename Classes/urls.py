from django.urls import path
from .views import classes, add_class, class_performance


urlpatterns = [
    path('list/', classes, name='classes'),
    path('add/', add_class, name='add-class'),
    path('performance/<int:clas>/', class_performance, name='class-performance')
]