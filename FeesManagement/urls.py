from django.urls import path
from .views import dues, add_due, add_due_payment, due_payments, parent_fees_payments, pay_child_fees, delete_due

urlpatterns = [
    path('list/', dues, name='dues'),
    path('New/', add_due, name='add-due'),
    path('add-payment/<int:due>/', add_due_payment, name='add-due-payment'),
    path('payments/<int:due>/', due_payments, name='due-payments'),
    path('parent/payments/', parent_fees_payments, name='parent-fees-payments'),
    path('pay/<int:child>/', pay_child_fees, name="pay-child-fees"),
    path('delete/<int:due>/', delete_due, name="delete-due")
]