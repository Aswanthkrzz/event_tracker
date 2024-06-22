from django.shortcuts import render
from booking.models import Booking
from event.models import Event
from vender.models import Vender
from food.models import Food
# from booking.models import
from auditorium.models import Auditorium
# Create your views here.

def register(request,idd):
    # qq= request.session["uid"]

    v=Auditorium.objects.get(aud_id=idd)

    context={
        'op':v,
    }


    if request.method == "POST":
        # hh=request.session["uid"]

        cbook=Booking.objects.filter(aud_id=idd,date=request.POST.get('date'))

        if len(cbook)<=0:
            jj=Auditorium()

            ob=Booking()
            ob.date=request.POST.get('date')
            ob.no_of_days=request.POST.get('DAYS')
            ob.time=request.POST.get('time')
            ob.booking_time=request.POST.get('type')
            # ob.fecilities=request.POST.get('feci')
            # ob.floors=request.POST.get('flor')
            ob.occasion=request.POST.get('function')
            # ob.amount=jj.amount
            ob.status="pending"
            ob.u_id=7
            ob.e_id=2
            ob.vend_id=3
            ob.aud_id=idd
            ob.save()
            obj="booked "
            con={
                'oo':obj
            }
            return render(request,'booking/booking.html',con)

    return render(request,'booking/booking.html',context)


def view(request):
    ob = Booking.objects.all()
    context = {
        'ok': ob,
    }
    return render(request,'booking/MANAGE_BOOKING.HTML',context)
def book(request,idd):

    obj = Booking.objects.get(ab_id=idd)
    obj.status ="book"
    obj.save()
    return view(request)
def manage(request):
    ob = Booking.objects.filter()
    context = {
        'ok': ob,

    }
    return render(request,'booking/AUD_BOOKING.html',context)
def accept(request,idd):
    obj = Booking.objects.get(ab_id=idd)
    obj.status ="accepted"
    obj.save()
    return manage(request)
    # return render(request,'payment/payment.html')

def reject(request,idd):
    obj = Booking.objects.get(ab_id=idd)
    obj.status ="reject"
    obj.save()
    return manage(request)

def viewstaus(request):
    # ee=request.session["uid"]
    ob = Booking.objects.filter(status="accepted")
    context = {
        'ok': ob,
    }
    return render(request,'booking/booking_statusview.html',context)
#
# def bookf(request,ee):
#     obj = Foodbook.objects.get(f_id=ee)
#     # ob=Food()
#     obj.image="image"
#     obj.place="place"
#     obj.user="ss"
#     obj.price ="book"
#     # ob.save()
#     obj.save()
#     return viewfood(request)

