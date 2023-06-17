from django.shortcuts import render, redirect
from .forms import SubscriptionForm
from Parents.models import Parent
from .models import Subscription
import requests
import json
from Payments.models import Payment
from django.contrib import messages
from Edumetrics.settings import culipa_headers as headers

url = "https://culipay.ug/initiate"

test_url = "https://test.culipay.ug/initiate"

def subscriptions(request):
    subscriptions = Subscription.objects.all()
    content = {
        'subscriptions': subscriptions
    }
    return render(request, 'subscriptions.html', content)

def subscribe_parent(request):
    form = SubscriptionForm(initial={'amount': 30000})
    content = {
        'form': form
    }
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                parent = Parent.objects.get(user__email=data['Parent'])
            except Parent.DoesNotExist:
                messages.success(request, 'The email entered is unregistered')
                return redirect('.')
            payload = json.dumps({
                "account": str(data['account']),
                "amount": '500',
                "currency": "UGX",
                "wallet": "MTNUG",
                "transactionID": "28531g2GHd1826etad",
                "merchant": "Edumetrics",
                "memo": "Edumetrics Subscription"
            })
            response = requests.request("POST", url, headers=headers, data=payload)
            if response.status_code == 200:
                try:
                    # Parse the response as JSON
                    response_data = json.loads(response.text)

                    # Print the parsed response
                    print(response_data)
                except json.JSONDecodeError as e:
                    print("Failed to decode response JSON:", str(e))
            else:
                print("Request failed with status code:", response.status_code)
            payment = Payment.objects.create(
                txid=response_data['culipaTxID'],
                amount=response_data['payment']['amount'],
                wallet=response_data['payment']['wallet'],
                Status=response_data['status'],
                account=response_data['payment']['account']
            )
            subscription = Subscription.objects.create(
                Parent=parent,
                Payment=payment,
                School=request.user.schooladministrator.current_school
            )
            parent.current_subscription = subscription
            parent.save()
            return redirect('payment-successful', subscription=subscription.id)
    else:
        return render(request, 'subscribe_parent.html', content)


def payment_successful(request, subscription):
    subscription = Subscription.objects.get(pk=subscription)
    content = {
        'subscription': subscription
    }
    return render(request, 'payment_successful.html', content)