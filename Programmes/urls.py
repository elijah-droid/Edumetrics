from django.urls import path
from .views import programmes, add_programme, students_on_programme, programme_fees_structure, programme_requirments

urlpatterns = [
    path('list/', programmes, name='programmes'),
    path('new/', add_programme, name='add-programme'),
    path('students/<int:programme>/', students_on_programme, name='students-on-programme'),
    path('fees-structure/<int:programme>/', programme_fees_structure, name='programme-fees-structure'),
    path('requirements/<int:programme>/', programme_requirments, name='programme-requirements')
]