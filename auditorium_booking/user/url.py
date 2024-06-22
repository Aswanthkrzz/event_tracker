from django.urls import path
from user import views
urlpatterns=[
    path('user/',views.user),
    path('view/',views.view),
    path('view_dealer/', views.view_dealer),
    path('update/(?P<idd>\w+)',views.update,name="updat"),
    path('delete/(?P<idd>\w+)',views.delete,name="delete"),
    path('aprv/(?P<idd>\w+)',views.accept,name='accpat'),
    path('reject/(?P<idd>\w+)',views.reject,name='rejct')

]