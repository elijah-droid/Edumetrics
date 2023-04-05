from django.urls import path
from .views import due_payments, add_due, add_due_payment

urlpatterns = [
    path('list/', due_payments, name='dues'),
    path('New/', add_due, name='add-due'),
    path('add-payment/<int:due>/', add_due_payment, name='add-due-payment')
]