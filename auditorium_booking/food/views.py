from django.shortcuts import render
from food.models import Food
from login.models import Login
from django.core.files.storage import FileSystemStorage

# Create your views here.
def post(request):
    if request.method=="POST":
        hh=Food()

        myfile = request.FILES["img"]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        hh.image=myfile.name
        hh.food_id=request.POST.get('funtion')
        hh.price=request.POST.get('price')
        hh.discription=request.POST.get('discription')
        hh.place=request.POST.get('place')
        hh.event_team_name=request.POST.get('event')
        hh.password=request.POST.get('password')
        hh.save()
        jj=Login()
        jj.username=hh.event_team_name
        jj.password=hh.password
        jj.type='catoring'
        jj.u_id=hh.f_if
        jj.save()
    return render(request,'food/post_food_dtailes.html')
def view(request):
    bb=Food.objects.all()
    context={
        'obj':bb
    }
    return render(request,'food/v_food_details.html',context)

