from django.urls import path 
from .views import subscriptions, subscribe_parent, payment_successful


urlpatterns = [
    path('paid/', subscriptions, name='subscriptions'),
    path('subscribe-parent/', subscribe_parent, name='subscribe-parent'),
    path('successful/<int:subscription>/', payment_successful, name='payment-successful')
]