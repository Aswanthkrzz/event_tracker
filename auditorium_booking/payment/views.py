
# import json
# from django.conf import settings
from django.shortcuts import render,redirect
# import razorpay
from .constants import PaymentStatus
# from django.views.decorators.csrf import csrf_exempt
from .models import Payment
from auditorium_booking.settings import RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET

# Create your views here.

def order_payment(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if not name:
            return redirect('hello')
        amount = request.POST.get("amount")
        # client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        # razorpay_order = client.order.create(
        #     {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
        # )
        # order = Payment.objects.create(
        #     name=name, amount=amount, provider_order_id=razorpay_order["id"]
        # )
        # order.save()
        return render(
            # request,
            # "payment/payment.html",
            # {
            #     "callback_url": "http://" + "127.0.0.1:8000" + "/payment/callback/",
            #     "razorpay_key": RAZORPAY_KEY_ID,
            #     "order": order,
            # },
        )
    return render(request, "payment/pay.html")

# @csrf_exempt
# def callback(request):
#     def verify_signature(response_data):
#         client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))
#         return client.utility.verify_payment_signature(response_data)

#     if "razorpay_signature" in request.POST:
#         payment_id = request.POST.get("razorpay_payment_id", "")
#         provider_order_id = request.POST.get("razorpay_order_id", "")
#         signature_id = request.POST.get("razorpay_signature", "")
#         order = Payment.objects.get(provider_order_id=provider_order_id)
#         order.payment_id = payment_id
#         order.signature_id = signature_id
#         order.save()
#         if not verify_signature(request.POST):
#             order.status = PaymentStatus.SUCCESS
#             order.save()
#             return render(request, "callback.html", context={"status": order.status})
#         else:
#             order.status = PaymentStatus.FAILURE
#             order.save()
#             return render(request, "callback.html", context={"status": order.status})
#     else:
#         payment_id = json.loads(request.POST.get("error[metadata]")).get("payment_id")
#         provider_order_id = json.loads(request.POST.get("error[metadata]")).get(
#             "order_id"
#         )
#         order = Payment.objects.get(provider_order_id=provider_order_id)
#         order.payment_id = payment_id
#         order.status = PaymentStatus.FAILURE
#         order.save()
#         return render(request, "callback.html", context={"status": order.status})

# @csrf_exempt
# def hello(request):
#     return render(request,'payment/callback.html')
