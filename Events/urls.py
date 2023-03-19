from django.urls import path
from .views import events, schedule_event

urlpatterns = [
    path('list/', events, name='events'),
    path('schedule/', schedule_event, name='schedule-event')
]
