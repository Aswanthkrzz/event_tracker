from django.shortcuts import render,redirect
from photography.models import Photography,PhotoFeedback
from login.models import Login
import datetime
from django.core.files.storage import FileSystemStorage
# Create your views here.
def photo(request):
    if request.method=="POST":
        dd=Photography()
        dd.studio_name=request.POST.get('name')
        dd.address=request.POST.get('addr')
        dd.email=request.POST.get('mail')
        dd.phone=request.POST.get('phone')
        # dd.image=request.POST.get('sds')

        myfile = request.FILES["sds"]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        dd.image = myfile.name

        dd.rate_photo=request.POST.get('prate')
        dd.rate_video=request.POST.get('vrate')
        dd.password=request.POST.get('password')
        dd.save()
    return render(request,'photography/reg_photo.html')
def viewphoto(request):
    gg=Photography.objects.all()
    context={
        'ok':gg
    }
    return render(request,'photography/view photograpfic team.html',context)
def managephoto(request):
    hh=Photography.objects.all()
    context={
        'ok':hh
    }
    return render(request,'photography/manage photo.html',context)
def blockphoto(request):
    hh=Login.objects.filter(type='photo')
    context={
        'ok':hh
    }
    return render(request,'photography/block.html',context)
def accepte(request,idd):
    ob = Photography.objects.get(ph_id=idd)
    ob.status="approved"
    ob.save()
    obj = Login()
    obj.username=ob.studio_name
    obj.password=ob.password
    obj.type='photo'
    obj.u_id=ob.ph_id
    obj.save()
    return managephoto(request)
def reject(request,idd):
    ob = Photography.objects.get(ph_id=idd)
    ob.status="reject"
    ob.save()
    return managephoto(request)
def delete(request,idd):
    obj = Photography.objects.get(ph_id=idd).delete()
    return managephoto(request)
def block1(request,idd):
    obj = Login.objects.filter(login_id=idd).delete()
    return blockphoto(request)

def updatephoto(request):
    hh=Photography.objects.all()
    context={
        'ok':hh
    }
    return render(request,'photography/update profile.html',context)

def update(request,idd):
    dd = Photography.objects.filter(ph_id=idd)
    context = {
        'ok': dd,
    }
    if request.method == "POST":
        dd = Photography.objects.get(ph_id=idd)
        dd.studio_name = request.POST.get('name')
        dd.address = request.POST.get('addr')
        dd.email = request.POST.get('mail')
        dd.phone = request.POST.get('phone')
        # dd.image=request.POST.get('sds')

        myfile = request.FILES["sds"]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        dd.image = myfile.name

        dd.rate_photo = request.POST.get('prate')
        dd.rate_video = request.POST.get('vrate')
        # dd.password = request.POST.get('password')
        dd.save()
        return updatephoto(request)
    return render(request,'photography/update.html',context)
# def dlte(request,idd):
#     ob = Photography.objects.get(ph_id=idd).delete()
#     return updatephoto(request)
# def delet(request,idd):
#     ov=Photography.objects.get(ph_id=idd).delete()
#     return updatephoto(request)

def photography_details(requst, id):
    obj = Photography.objects.get(ph_id=id)
    feedbacks = PhotoFeedback.objects.filter(ph_id=id)
    context={
        'photography':obj,
        "feedbacks": feedbacks
    }
    return render(requst, 'photography/photography_details.html', context)


def add_feedback(request, id):
    kk=request.session["uid"]
    if request.method=="POST":
        ob=PhotoFeedback()
        ob.feedback=request.POST.get('feedback')
        ob.u_id=kk
        ob.ph_id = id
        ob.date_time=datetime.datetime.now()
        ob.save()
        return redirect(f'photography_details/{id}')
    return render(request,'photography/feedback.html')

def feedback(requst):
    obj = Photography.objects.all()
    feedbacks = PhotoFeedback.objects.all()
    context={
        'photography':obj,
        "feedbacks": feedbacks
    }
    return render(requst, 'photography/feedback1.html', context)


