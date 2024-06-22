from django.urls import path
from dealer import views
urlpatterns=[
    path('reg/',views.register),
    path('view/',views.view),
    path('manage/',views.manage),
    path('accept/(?P<idd>\w+)', views.accept, name='accept'),
    path('reject/(?P<idd>\w+)', views.reject, name='reject'),


]