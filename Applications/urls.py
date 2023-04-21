from django.urls import path
from .views import schools_listing, apply, parent_applications, school_applications, applicant_profile


urlpatterns = [
    path('schools-listing/', schools_listing, name='schools-listing'),
    path('apply/<int:school>/', apply, name='apply-online'),
    path('parent-applications/', parent_applications, name='parent-applications'),
    path('school-applications/', school_applications, name='school-applications'),
    path('applicant-profile/<int:application>/', applicant_profile, name='applicant-profile')
]