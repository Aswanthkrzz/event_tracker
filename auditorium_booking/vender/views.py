from django.shortcuts import render,redirect
from vender.models import Vender,EventFeedback
from login.models import Login
import datetime
from django.core.files.storage import FileSystemStorage
# Create your views here.
def vennder(request):
    if request.method == "POST":
        obj=Vender()
        obj.phone=request.POST.get('phone')
        obj.name=request.POST.get('name')
        obj.email=request.POST.get('mail')
        obj.adress=request.POST.get('addr')
        obj.password=request.POST.get('pass')
        obj.place = request.POST.get('place')
        obj.lisence_id = request.POST.get('ld')
        # obj.image=request.POST.get('sds')

        myfile = request.FILES["sds"]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.image = myfile.name

        obj.u_id=1

        # ob.u = request.POST.get('name')
        obj.password = request.POST.get('pass')
        obj.save()

    return render(request,'vender/vender.HTML')

def vview(request):
    hh=request.session["uid"]
    kk=Vender.objects.filter(vend_id=hh)
    context={
        'ok':kk,
    }
    return render(request,'vender/VIEW VENDER.HTML',context)


def view_vender(request):
    ob=Vender.objects.all()
    context={
        'ok':ob,
    }
    return render(request,'vender/view_vender.html',context)
def reject_vender(request):
    ob=Login.objects.filter(type="event")
    context={
        'ok':ob,
    }
    return render(request,'vender/reject_vender.html',context)
def update(request,idd):
    ob = Vender.objects.filter( vend_id=idd)
    context = {
        'ok': ob,
    }
    if request.method == "POST":
        ob=Vender.objects.get( vend_id=idd)
        ob.phone=request.POST.get('phone')
        ob.name=request.POST.get('name')
        ob.email=request.POST.get('mail')
        ob.adress=request.POST.get('addr')
        ob.password=request.POST.get('pass')
        ob.place = request.POST.get('place')

        myfile = request.FILES["sds"]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        ob.image = myfile.name

        # ob.password=request.POST.get('pass')
        ob.save()
        return vview(request)
    return render(request,'vender/vendder_update.HTML',context)
def delete(requst,idd):
    ob=Vender.objects.get(vend_id=idd).delete()
    return vview(requst)
def accept(request,idd):
    obj=Vender.objects.get(vend_id=idd)
    obj.status='aproved'
    obj.save()
    vv = Login()
    vv.username = obj.name
    vv.password = obj.password
    vv.type = 'event'
    vv.u_id = obj.vend_id
    vv.save()

    return view_vender(request)
def reject(request,idd):
    ob = Login.objects.get(login_id=idd).delete()
    return reject_vender(request)
def search(request):
    if request.method=="POST":
        v=request.POST.get('name')
        if Vender.objects.filter(name__icontains=v).exists():
            obj=Vender.objects.filter(name__icontains=v)
            context={
                'objval':obj,
            }


            return render(request, 'vender/searchevent.html',context)
        return render(request, 'vender/searchevent.html')
    return render(request, 'vender/searchevent.html')
def reject1(request,idd):
    obj=Vender.objects.get(vend_id=idd)
    obj.status='rejected'
    obj.save()
    return view_vender(request)
def delete1(request,idd):
    ob = Vender.objects.get(vend_id=idd).delete()
    return view_vender(request)
def vender_details(requst, id):
    obj = Vender.objects.get(vend_id=id)
    feedbacks = EventFeedback.objects.filter(vend_id=id)
    context={
        'vender':obj,
        "feedbacks": feedbacks
    }
    return render(requst, 'vender/vender_details.html', context)


def add_feedback(request, id):
    kk=request.session["uid"]
    if request.method=="POST":
        ob=EventFeedback()
        ob.feedback=request.POST.get('feedback')
        ob.u_id=kk
        ob.vend_id = id
        ob.date_time=datetime.datetime.now()
        ob.save()
        return redirect(f'vender_details/{id}')
    return render(request,'vender/feedback.html')
def feedback1(requst,):
    obj = Vender.objects.all()
    feedbacks = EventFeedback.objects.all()
    context={
        'vender':obj,
        "feedbacks": feedbacks
    }
    return render(requst, 'vender/view_feedback1.html', context)


