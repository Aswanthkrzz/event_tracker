from django.shortcuts import render

# Create your views here.


def admin_home(request):
    return render(request,'temp/admin_home.html')
def dealer_home(request):
    return render(request,'temp/dealer_home.html')
def mainhome(request):
    return render(request,'temp/mainhome.html')
def user_home(request):
    return render(request,'temp/user_home.html')
# def admin(request):
#     return render(request,'temp/admin.html')
# def user(request):
#     return render(request,'temp/user.html')
# def dealer(request):
#     return render(request,'temp/dealer.html')
# def aud(request):
#     return render(request,'temp/admin.html')
def haud(request):
    return render(request,'temp/auditorium_home.html')
def photo(request):
    return render(request,'temp/photography.html')
def about(request):
    return render(request,'temp/about.html')
def service(request):
    return render(request,'temp/service.html')