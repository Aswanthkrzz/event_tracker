from django.urls import path
from temp import views
urlpatterns=[
    path('mainhome/', views.mainhome),
    path('adminhome/',views.admin_home,),
    path('dealerhome/', views.dealer_home),
    path('', views.mainhome),
    path('userhome/', views.user_home),
    path('audh/', views.haud),
    # url(r'^admin/',views.admin),
    # url(r'^user/', views.user),
    # url(r'^dealer/', views.dealer),
    # url(r'^aud/', views.aud),
    path('photography/', views.photo),
    path('about/', views.about),
    path('service/', views.service)



]