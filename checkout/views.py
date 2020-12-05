from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm
from tickets.forms import TicketsForm
from tickets.models import Ticket
from django.conf import settings
from accounts.views import login, index 
from django.utils import timezone
import stripe
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method == "POST":
        payment_form = MakePaymentForm(request.POST)

        if  payment_form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount=500,
                    currency="EUR",
                    description="Thank you for your contribution, it will help our site tremendously" and request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()

    return render(request, "checkout.html", {"payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})