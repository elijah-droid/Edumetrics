from django.urls import path
from .views import dues, add_due, add_due_payment, due_payments

urlpatterns = [
    path('list/', dues, name='dues'),
    path('New/', add_due, name='add-due'),
    path('add-payment/<int:due>/', add_due_payment, name='add-due-payment'),
    path('payments/<int:due>/', due_payments, name='due-payments')
]