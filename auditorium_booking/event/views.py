from django.shortcuts import render
from  event.models import Event
from  login.models import Login

# Create your views here.

def event(request):
    if request.method == "POST":
        ob=Event()
        ob.name=request.POST.get('ename')
        ob.adress=request.POST.get('addressemp')
        ob.contact_number=request.POST.get('phone')
        ob.date=request.POST.get('date')
        ob.time = request.POST.get('time')
        # ob.username = request.POST.get('unameemp')
        # ob.password = request.POST.get('pswdemp')
        ob.save()
        # oo=Login()
        # oo.username=ob.username
        # oo.password=ob.password
        # oo.type='event'
        # oo.u_id=ob.e_id
        # oo.save()
    return render(request,'event/event_reg.html')
def search(request):
    if request.method=="POST":
        v=request.POST.get('name')
        if Event.objects.filter(adress__icontains=v).exists():
            obj=Event.objects.filter(adress__icontains=v)
            context={
                'objval':obj,
            }


            return render(request, 'event/searchevent.html',context)
        return render(request, 'event/searchevent.HTML')
    return render(request, 'event/searchevent.HTML')
