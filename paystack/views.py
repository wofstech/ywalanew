
import json
import base64
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.utils import timezone
from django.http import JsonResponse
from django.views.generic import RedirectView, TemplateView
# Create your views here.
from . import settings, signals, utils
from .signals import payment_verified
from .utils import load_lib
from django.contrib import messages
from django.dispatch import receiver
from houses.models import Myhouses


def verify_payment(request, order):
    
    amount = request.GET.get('amount')
    txrf = request.GET.get('trxref')
    PaystackAPI = load_lib()
    paystack_instance = PaystackAPI()
    response = paystack_instance.verify_payment(txrf, amount=int(amount))
    if response[0]:
        payment_verified.send(
            sender=PaystackAPI,
            username = request.user,
            ref=txrf, amount=int(amount) / 100, order=order)
        return redirect(reverse('paystack:successful_verification', args=[order]))
    return redirect(reverse('paystack:failed_verification', args=[order]))


class FailedView(RedirectView):
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        if settings.PAYSTACK_FAILED_URL == 'paystack:failed_page':
            return reverse(settings.PAYSTACK_FAILED_URL)
        return settings.PAYSTACK_FAILED_URL


def success_redirect_view(request, order_id):
    url = settings.PAYSTACK_SUCCESS_URL
    if url == 'paystack:success_page':
        url = reverse(url)
    return redirect(url, permanent=True)

def failure_redirect_view(request, order_id):
    url = settings.PAYSTACK_FAILED_URL
    if url == 'paystack:failed_page':
        url = reverse(url)
    return redirect(url, permanent=True)

class SuccessView(RedirectView):
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        if settings.PAYSTACK_SUCCESS_URL == 'paystack:success_page':
            return reverse(settings.PAYSTACK_SUCCESS_URL)
        return settings.PAYSTACK_SUCCESS_URL


def webhook_view(request):
    # ensure that all parameters are in the bytes representation
    digest = utils.generate_digest(request.body)
    signature = request.META['HTTP_X_PAYSTACK_SIGNATURE']
    if digest == signature:
        payload = json.loads(request.body)
        signals.event_signal.send(
            sender=request, event=payload['event'], data=payload['data'])
    return JsonResponse({'status': "Success"})
