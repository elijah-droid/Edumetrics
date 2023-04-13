from django.urls import path
from .views import classes, add_class, class_performance, class_streams, class_students, class_profile


urlpatterns = [
    path('list/', classes, name='classes'),
    path('add/', add_class, name='add-class'),
    path('performance/<int:clas>/', class_performance, name='class-performance'),
    path('streams/<int:clas>/', class_streams, name='class-streams'),
    path('students/<int:clas>/', class_students, name='class-students'),
    path('profile/<int:clas>/', class_profile, name='class-profile')
]