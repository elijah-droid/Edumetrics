from django.shortcuts import render, redirect
from .forms import PaymentDueForm, PaymentForm, ParentPaymentForm
from .models import PaymentDue
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import send_mail
from Edumetrics.settings import culipa_headers as headers
import requests
import json

url = "https://culipay.ug/initiate"

def dues(request):
    dues = PaymentDue.objects.all()
    context = {
        'dues': dues
    }
    return render(request, 'dues.html', context)

def due_payments(request, due):
    due = request.user.schooladministrator.current_school.Dues.get(pk=due)
    context = {
        'due': due
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
            due.Classes.set(form.cleaned_data['Classes'])
            due.School.Dues.add(due)
        return redirect('dues')
    else:
        return render(request, 'add_due.html', context)


def add_due_payment(request, due):
    form = PaymentForm()
    due = request.user.schooladministrator.current_school.Dues.get(id=due)
    form.fields['Student'].queryset = request.user.schooladministrator.current_school.students.all()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            memo = f"{request.user.schooladministrator.current_school} {due.Reason}"
            payload = json.dumps({
                "account": str(form.cleaned_data['payment_number']),
                "amount": form.cleaned_data['Amount'],
                "currency": "UGX",
                "wallet": "MTNUG",
                "transactionID": "28531g2GHd1826etad",
                "merchant": "Edumetrics",
                "memo": memo
            })
            response = requests.request("POST", url, headers=headers, data=payload)
            print(json.dumps(response.text))
            payment = form.save(commit=False)
            payment.Due = due
            payment.paid_via = 'School'
            payment.save()
            due.Payments.add(payment)
            payment.parent.Fees_Payments.add(payment)
            message = f'''
            A total amount of {payment.Amount} UGX was paid to {request.user.schooladministrator.current_school} 
            via the school For {payment.Student} {payment.Due.Reason}.
            '''
            send_mail(
                f'Fees Payment Made to {request.user.schooladministrator.current_school}',
                message,
                'edumetrics@sparklehandscs.com',
                [payment.parent.user.email]
            )
            return redirect('due-payments', due=due.id)
    else:
        return render(request, 'add_due_payment.html', context)


def pay_child_fees(request, child):
    child = request.user.parent.relationships.get(Child__id=child).Child
    form = ParentPaymentForm()
    form.fields['Due'].queryset = child.school.Dues.filter(Classes=child.Class)
    context = {
        'form': form,
        'child': child
    }
    if request.method == 'POST':
        form = ParentPaymentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            due = data['Due']
            payment = due.Payments.create(
                parent=request.user.parent,
                Student=child,
                Amount=data['Amount'],
                Due=due,
                Method='Mobile Money',
                Paid_Via='Mobile'
            )
            request.user.parent.Fees_Payments.add(payment)
            messages.success(request, 'Payment Made Successfully.')
            message = f'''
            A total amount of {payment.Amount} UGX was paid to {child.school} 
            via the school For {payment.Student} {payment.Due.Reason}.
            '''
            send_mail(
                f'Fees Payment Made to {child.school}',
                message,
                'edumetrics@sparklehandscs.com',
                [payment.parent.user.email]
            )
            return redirect('parent-fees-payments')
    else:
        return render(request, 'pay_child_fees.html', context)


def parent_fees_payments(request):
    return render(request, 'parent_fees_payments.html')

def delete_due(request, due):
    try:
        due = request.user.schooladministrator.current_school.Dues.get(id=due)
        due.delete()
    except:
        pass
    return redirect('dues')