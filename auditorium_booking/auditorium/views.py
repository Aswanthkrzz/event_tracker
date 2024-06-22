from django.shortcuts import render,redirect
from auditorium.models import Auditorium, AuditoriumFeedback
from login.models import Login
from django.core.files.storage import FileSystemStorage
import datetime

# Create your views here.
def register(request):
    # o=request.session["uid"]
    if request.method=="POST":
        ob=Auditorium()
        ob.amount=request.POST.get('amt')
        ob.email=request.POST.get('mail')
        ob.d_id=1
        ob.name=request.POST.get('name')
        ob.phone=request.POST.get('phone')
        ob.place=request.POST.get('place')
        ob.address=request.POST.get('addr')
        ob.services=request.POST.get('services')
        ob.phone=request.POST.get('phone')

        myfile = request.FILES["sds"]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        ob.image = myfile.name

        ob.password=request.POST.get('password')
        ob.status="pending"
        ob.save()
        # obj=Login()
        # obj.username=ob.name
        # obj.password=ob.password
        # obj.type='auditorium'
        # obj.u_id=ob.aud_id
        # obj.save()
    return render(request,'auditorium/AUDITORIUM.HTML')

# def search(request):
#     if request.method=="POST":
#         np=request.POST.get('name')
#         obj=Auditorium.objects.filter(place__icontains=np)
#         context={
#             'objval':obj,
#         }
#         return render(request,'auditorium/SEARCH.HTML',context)
#     return render(request,'auditorium/SEARCH.HTML')
def search(request):
    if request.method=="POST":
        v=request.POST.get('name')
        if Auditorium.objects.filter(place__icontains=v).exists():
            obj=Auditorium.objects.filter(place__icontains=v)
            context={
                'objval':obj,
            }


            return render(request, 'auditorium/SEARCH.HTML',context)
        return render(request, 'auditorium/SEARCH.HTML')
    return render(request, 'auditorium/SEARCH.HTML')

def viewsearch(request):
    ob = Auditorium.objects.all()
    context = {
        'ok': ob,
    }
    return render(request,'auditorium/VIEW SEARCH.HTML',context)
def updprof(request):
    hh=request.session["uid"]
    ob = Auditorium.objects.filter(aud_id=hh)
    context = {
        'ok': ob,
    }
    return render(request,'auditorium/profile update.html',context)

def update(request,idd):
    ob = Auditorium.objects.filter( aud_id=idd)
    context = {
        'ok': ob,
    }
    if request.method == "POST":
        ob=Auditorium.objects.get( aud_id=idd)
        ob.phone=request.POST.get('phone')
        ob.name=request.POST.get('name')
        ob.email=request.POST.get('mail')
        ob.place=request.POST.get('addr')
        # ob.password=request.POST.get('pass')
        # ob.place = request.POST.get('place')
        # ob.password=request.POST.get('pass')
        ob.save()
        return updprof(request)
    return render(request,'auditorium/update.HTML',context)
def delete1(requst,idd):
    ob=Auditorium.objects.get(aud_id=idd).delete()
    return updprof(requst)

def accepted(request,idd):
    ob = Auditorium.objects.get(aud_id=idd)
    ob.status="approved"
    ob.save()
    obj = Login()
    obj.username = ob.email
    obj.password = ob.password
    obj.type = 'auditorium'
    obj.u_id = ob.aud_id
    obj.save()
    return viewsearch(request)
def rejected(request,idd):
    ob = Auditorium.objects.get(aud_id=idd)
    ob.status="rejected"
    ob.save()
    return viewsearch(request)
def delete(request,idd):
    obj = Auditorium.objects.get(aud_id=idd).delete()
    return viewsearch(request)
def block(request,idd):
    obj = Login.objects.get(login_id=idd).delete()
    return vblock(request)
def vblock(request):
    ob = Login.objects.filter(type='auditorium')
    context = {
        'ok': ob,
    }
    return render(request,'auditorium/block.HTML',context)

def auditorium_details(requst, id):
    obj = Auditorium.objects.get(aud_id=id)
    feedbacks = AuditoriumFeedback.objects.filter(aud_id=id)
    context={
        'auditorium':obj,
        "feedbacks": feedbacks
    }
    return render(requst, 'auditorium/auditorium_details.html', context)


def add_feedback(request, id):
    kk=request.session["uid"]
    if request.method=="POST":
        ob=AuditoriumFeedback()
        ob.feedback=request.POST.get('feedback')
        ob.u_id=kk
        ob.aud_id = id
        ob.date_time=datetime.datetime.now()
        ob.save()
        return redirect(f'auditorium_details/{id}')
    return render(request,'auditorium/feedback.html')
def feedback1(requst):
    obj = Auditorium.objects.get()
    feedbacks = AuditoriumFeedback.objects.filter()
    context={
        'auditorium':obj,
        "feedbacks": feedbacks
    }
    return render(requst, 'auditorium/view_feedback1.html', context)

