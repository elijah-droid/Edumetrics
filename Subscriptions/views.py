from django.shortcuts import render, redirect
from .forms import SubscriptionForm
from Parents.models import Parent
from .models import Subscription

def subscriptions(request):
    subscriptions = Subscription.objects.all()
    content = {
        'subscriptions': subscriptions
    }
    return render(request, 'subscriptions.html', content)

def subscribe_parent(request):
    form = SubscriptionForm()
    content = {
        'form': form
    }
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            parent = Parent.objects.first()
            subscription = form.save(commit=False)
            subscription.Parent = parent
            subscription.School = request.user.schooladministrator.current_school
            subscription.save()
            return redirect('payment-successful', subscription=subscription.id)
    else:
        return render(request, 'subscribe_parent.html', content)


def payment_successful(request, subscription):
    subscription = Subscription.objects.get(pk=subscription)
    content = {
        'subscription': subscription
    }
    return render(request, 'payment_successful.html', content)