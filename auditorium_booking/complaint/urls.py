from django.shortcuts import render
from complaint import views
from django.urls import path

urlpatterns = [
    path('complaint/', views.complaint),
    path('reply/(?P<idd>\w+)', views.reply,name='reply'),
    path('view_comp/', views.view_comp),
    path('view_comp_rply/', views.view_complaint)
   ]

