from django.urls import path
from .views import tallies, tally


urlpatterns = [
    path('list/', tallies, name='tallies'),
    path('tally/', tally, name='tally')
]