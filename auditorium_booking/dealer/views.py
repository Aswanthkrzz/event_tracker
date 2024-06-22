from django.shortcuts import render
from dealer.models import Dealer
from login.models import Login
# Create your views here.
def register(request):
    if request.method == "POST":
        ob=Dealer()
        ob.d_address=request.POST.get('addr')
        ob.d_name=request.POST.get('name')
        ob.phone=request.POST.get('phone')
        ob.email = request.POST.get('mail')
        ob.status="pending"
        ob.save()
        oo=Login()
        oo.username=request.POST.get('name')
        oo.password=request.POST.get('mail')
        oo.type='dealer'
        oo.u_id=ob.d_id
        oo.save()
    return render(request,'dealer/DEALER.HTML')

def view(request):
    ob = Dealer.objects.all()
    context = {
        'ok': ob,
    }
    return render(request,'dealer/view dealer.html',context)

def manage(request):

    ob = Dealer.objects.filter(status="pending")
    context = {
        'ok': ob,
    }
    return render(request,'dealer/manage_dealer.html',context)
def accept(request,idd):
    obj = Dealer.objects.get(d_id=idd)
    obj.status='áccept'
    obj.save()
    return manage(request)
def reject(request,idd):
    obj = Dealer.objects.get(d_id=idd)
    obj.status ="reject"
    obj.save()
    return manage(request)
