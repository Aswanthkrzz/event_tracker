from django.shortcuts import render
from order.models import Order
from auditorium.models import Auditorium
import datetime
from vender.models import Vender
# Create your views here.

def register(request,idd):
    qq= request.session["uid"]

    v=Vender.objects.get(vend_id=idd)

    context={
        'op':v,
    }


    if request.method == "POST":

        cbook=Order.objects.filter(vend_id=idd,date=request.POST.get('date'))

        if len(cbook)<=0:
            ob=Order()
            ob.date=datetime.date.today()
            ob.name=request.POST.get('DAYS')
            ob.time=datetime.datetime.now()
            ob.amount=request.POST.get('bdj')
            ob.program=request.POST.get('pro')
            # ob.fecilities=request.POST.get('feci')
            # ob.floors=request.POST.get('flor')
            ob.address=request.POST.get('function')
            ob.status="pending"
            ob.u_id=qq
            # ob.e_id=2
            ob.instrument_id=1
            # ob.order_id=1
            ob.vend_id=idd
            ob.aud_id=1
            ob.save()
            obj="booked "
            con={
                'oo':obj
            }
            return render(request,'order/booking.html',con)

    return render(request,'order/booking.html',context)


def view(request):
    ob = Order.objects.all()
    context = {
        'ok': ob,
    }
    return render(request,'order/MANAGE_BOOKING.HTML',context)
def book(request,idd):

    obj = Order.objects.get(order_id=idd)
    obj.status ="book"
    obj.save()
    return view(request)
def manage(request):
    ob = Order.objects.filter()
    context = {
        'ok': ob,

    }
    return render(request,'order/AUD_BOOKING.html',context)
def accept(request,idd):
    obj = Order.objects.get(ap_id=idd)
    obj.status ="accepted"
    obj.save()
    return manage(request)

def reject(request,idd):
    obj = Order.objects.get(ap_id=idd)
    obj.status ="reject"
    obj.save()
    return manage(request)

def viewstaus(request):
    # ee=request.session["uid"]
    ob = Order.objects.filter(status='accepted')
    context = {
        'ok': ob,
    }
    return render(request,'order/booking_statusview.html',context)
