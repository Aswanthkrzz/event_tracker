from django.urls import path
from vender import views
urlpatterns=[
    path('vender/',views.vennder),
    path('vview/',views.vview),
    path('view_vender/', views.view_vender),
    path('reject_vender/', views.reject_vender),
    path('search/', views.search),
    path('update/(?P<idd>\w+)',views.update,name="updat1"),
    path('delete/(?P<idd>\w+)',views.delete,name="delete1"),
    path('aprv1/(?P<idd>\w+)',views.accept,name='accpat1'),
    path('block/(?P<idd>\w+)',views.reject,name='blocked'),
    path('reject/(?P<idd>\w+)',views.reject1,name='rejct1'),
    path('delete1/(?P<idd>\w+)',views.delete1,name='deletev'),
    path('vender_details/(?P<id>\w+)', views.vender_details, name='vender_details'),
    path('feedback/(?P<id>\w+)', views.add_feedback, name='vender_feedback'),
    path('feedback1/', views.feedback1, name='feedback1')
]