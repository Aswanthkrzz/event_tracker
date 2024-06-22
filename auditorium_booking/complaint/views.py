from django.shortcuts import render
from complaint.models import Complaint
import datetime

def complaint(request):
    if request.method=="POST":
        obj=Complaint()
        obj.complaint=request.POST.get('compl')
        obj.date=datetime.date.today()
        obj.patient_id="1"
        obj.replay="pending"
        obj.save()
        obj = "booked "
        con = {
            'oo': obj
        }
    return render(request, 'complaint/complaint.html')

def reply(request,idd):
    o=Complaint.objects.get(complaint_id=idd)
    context={
        'obval':o
    }
    if request.method=="POST":

        obj=Complaint.objects.get(complaint_id=idd)

        obj.replay=request.POST.get('reply')
        obj.save()
        return view_comp(request)
    return render(request, 'complaint/postreplay.html',context)


def view_complaint(request):
    ff=request.session["uid"]
    obj=Complaint.objects.filter(complaint_id=ff)
    context={
        'objval':obj
    }

    return render(request,'complaint/post complaint and post replay.html',context)

def view_comp(request):
    obj=Complaint.objects.filter(replay='pending')
    context={
        'objval' : obj
    }
    return render(request,'complaint/view complaint and post reply.html',context)





