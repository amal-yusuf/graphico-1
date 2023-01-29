from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Lz3N7GcnROZLgz31xnLgi9o9sH6wgFbqVeGS2nB0TKrIC1gZw3FePj2weupYWdmePvj840c0cGl1vuWNDWJy0Cf00NCn6ArJQ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
