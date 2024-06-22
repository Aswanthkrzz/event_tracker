"""auditorium_booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from django.conf.urls import url,include
from login import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',include('login.url')),
    path('auditorium/',include('auditorium.url')),
    path('booking/',include('booking.url')),
    path('dealer/',include('dealer.url')),
    path('payment/',include('payment.url')),
    path('user/',include('user.url')),
    path('temp/',include('temp.url')),
    path('vender/',include('vender.url')),
    path('decoration/',include('decoration.url')),
    path('food/',include('food.url')),
    path('event/',include('event.url')),
    path('complaint/',include('complaint.urls')),
    path('order/',include('order.urls')),
    path('photobook/',include('foodbooking.url')),
    path('feed/',include('feedback.urls')),
    path('photo/',include('photography.urls')),
    path('',include('temp.url')),
    # path('$',views.login),

]
