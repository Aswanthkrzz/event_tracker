from django.shortcuts import render
from decoration.models import Decoration
from django.core.files.storage import FileSystemStorage

# Create your views here.
def post(request):
    if request.method=="POST":
        hh=Decoration()

        myfile = request.FILES["img"]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        hh.image=myfile.name
        hh.finction_id=request.POST.get('funtion')
        hh.price=request.POST.get('price')
        hh.discription=request.POST.get('discription')
        hh.place=request.POST.get('place')
        hh.event_team_name=request.POST.get('event')
        hh.save()
    return render(request,'decoration/post_decoration.html')
def view(request):
    bb=Decoration.objects.all()
    context={
        'obj':bb
    }
    return render(request,'decoration/v_decoration.html',context)
