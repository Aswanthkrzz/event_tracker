from django.shortcuts import render
from feedback.models import Feedback
import datetime
# Create your views here.
def feedback(request):
    # ss = request.session["uid"]
    if request.method=="POST":
        ob=Feedback()
        ob.feedback=request.POST.get('feedback')
        ob.u_id=1
        ob.date=datetime.datetime.today()
        ob.time=datetime.datetime.now()
        ob.save()
    return render(request,'feedback/feedback.html')
def viewfeed(requset):
    object=Feedback.objects.all()
    context={
        'aaa':object
    }
    return render(requset,'feedback/view_feedback.html',context)

def viewfeed1(requset):
    object=Feedback.objects.all()
    context={
        'aaa':object
    }
    return render(requset,'feedback/view_feedback1.html',context)
def viewfeed2(requset):
    object=Feedback.objects.all()
    context={
        'aaa':object
    }
    return render(requset,'feedback/view_feedback2.html',context)