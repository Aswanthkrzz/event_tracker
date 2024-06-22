from django.shortcuts import render
from foodbooking.models import Photobook

# Create your views here.
def food(request,idd):
    hh = request.session["uid"]
    if request.method=="POST":
        # ob = Foodbook.objects.get(f_id=idd)
        ob=Photobook()
        ob.date=request.POST.get('date')
        ob.time=request.POST.get('time')
        ob.place=request.POST.get('placy')
        ob.service=request.POST.get('type')
        ob.ph_id=hh
        ob.u_id=1
        ob.status='pending'
        ob.save()
    return render(request,'foodbooking/foodbooking.html')
def manage(request):
    ob = Photobook.objects.filter()
    context = {
        'ok': ob,

    }
    return render(request,'foodbooking/foodmanage.html',context)
def accepty(request,idd):
    obj = Photobook.objects.get(f_id=idd)
    obj.status ="accepted"
    obj.save()
    return manage(request)

def rejecty(request,idd):
    obj = Photobook.objects.get(f_id=idd)
    obj.status ="reject"
    obj.save()
    return manage(request)
def status(request):
    ob = Photobook.objects.filter()
    context = {
        'ok': ob,

    }
    return render(request,'foodbooking/booking status.html',context)

#
