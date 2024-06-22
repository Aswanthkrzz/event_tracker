from django.shortcuts import render
from login.models import Login
# Create your views here.
def login(request):
    if request.method == "POST":
        uname = request.POST.get("name")
        passw = request.POST.get("pass")
        obj = Login.objects.filter(username=uname,password=passw)
        tp = ""
        for ob in obj:
            tp = ob.type
            uid = ob.u_id
            if tp == "admin":
                request.session["uid"] = uid
                return render(request, 'temp/admin_home.html')
            elif tp == "event":
                request.session["uid"] = uid
                return render(request, 'temp/dealer_home.html')
            elif tp == "auditorium":
                request.session["uid"] = uid
                return render(request, 'temp/auditorium_home.html')
            elif tp == "user":
                request.session["uid"] = uid
                return render(request, 'temp/user_home.html')
            elif tp == "photo":
                request.session["uid"] = uid
                return render(request, 'temp/photography.html')
            # else:
        objlist = "Username or Password incorrect... Please try again...!"
        context = {
            'msg': objlist,
            }
        return render(request, 'login/login.html', context)
    return render(request,'login/login.html')


