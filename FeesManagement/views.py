from django.shortcuts import render, redirect
from .forms import PaymentDueForm, PaymentForm
from .models import PaymentDue

def due_payments(request):
    dues = PaymentDue.objects.all()
    context = {
        'dues': dues
    }
    return render(request, 'due_payments.html', context)

def add_due(request):
    form = PaymentDueForm()
    form.fields['Classes'].queryset = request.user.schooladministrator.current_school.classes.all()
    context = {
       'form': form,
    }
    if request.method == 'POST':
        form = PaymentDueForm(request.POST) 
        if form.is_valid():
            due = form.save(commit=False)
            due.School = request.user.schooladministrator.current_school
            due.save()
            due.School.Dues.add(due)
        return redirect('dues')
    else:
        return render(request, 'add_due.html', context)


def add_due_payment(request, due):
    form = PaymentForm()
    form.fields['parent'].queryset = request.user.schooladministrator.current_school.Parents.all()
    form.fields['Student'].queryset = request.user.schooladministrator.current_school.students.all()
    context = {
        'form': form
    }
    if request.method == 'POST':
        payment = form.save(commit=False)

    else:
        return render(request, 'add_due_payment.html', context)


def pay_child_fees(request, child):
    
    return render(request, 'pay_child_fees.html', context)
    