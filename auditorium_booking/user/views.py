from django.shortcuts import render
from user.models import User
from login.models import Login
# Create your views here.
def user(request):
    if request.method == "POST":
        ob=User()
        ob.phone=request.POST.get('phone')
        ob.name=request.POST.get('name')
        ob.email=request.POST.get('mail')
        ob.address=request.POST.get('addr')
        ob.password=request.POST.get('pass')
        ob.place = request.POST.get('place')
        # ob.username = request.POST.get('uname')
        ob.password = request.POST.get('pass')
        ob.status='pending'
        ob.save()
        vv = Login()
        vv.username = ob.name
        vv.password = ob.password
        vv.type = 'user'
        vv.u_id = ob.u_id
        vv.save()

    return render(request,'user/USER.HTML')

def view(request):
    ob=User.objects.filter(status='pending')
    context={
        'ok':ob,
    }
    return render(request,'user/VIEW USER.HTML',context)


def view_dealer(request):
    ob=User.objects.all()
    context={
        'ok':ob,
    }
    return render(request,'user/view user dealer.html',context)
def update(request,idd):
    ob = User.objects.filter(u_id=idd)
    context = {
        'ok': ob,
    }
    if request.method == "POST":
        ob=User.objects.get(u_id=idd)
        ob.phone=request.POST.get('phone')
        ob.name=request.POST.get('name')
        ob.email=request.POST.get('mail')
        ob.address=request.POST.get('addr')
        ob.password=request.POST.get('pass')
        ob.place = request.POST.get('place')
        # ob.password=request.POST.get('pass')
        ob.save()
        return view(request)
    return render(request,'user/user_update.HTML',context)
def delete(requst,idd):
    ob=User.objects.get(u_id=idd).delete()
    return view_dealer(requst)
def accept(request,idd):
    ob=User.objects.get(u_id=idd)
    ob.status='aproved'
    ob.save()

    return view_dealer(request)
def reject(request,idd):
    obj=User.objects.get(u_id=idd)
    obj.status='rejected'
    obj.save()
    ob=Login()
    ob.type='blocked'
    ob.save
    return view_dealer(request)