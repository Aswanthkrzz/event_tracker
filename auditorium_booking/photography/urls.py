from django.urls import path
from photography import views

urlpatterns=[
    path('reg/',views.photo),
    path('view/',views.viewphoto),
    path('manage/',views.managephoto),
    path('blockp/',views.blockphoto),
    path('updatephoto/',views.updatephoto),
    path('accepto/(?P<idd>\w+)',views.accepte,name='accepto'),
    path('rejecti/(?P<idd>\w+)',views.reject,name='rejecti'),
    path('delete/(?P<idd>\w+)',views.delete,name='deleted'),
    path('block1/(?P<idd>\w+)',views.block1,name='block1'),
    path('update/(?P<idd>\w+)',views.update,name='upd'),
    # url('dlte/(?P<idd>\w+)',views.delet,name='dlt'),
    path('photography_details/(?P<id>\w+)', views.photography_details, name='photography_details'),
    path('feedback/(?P<id>\w+)', views.add_feedback, name='photography_feedback'),
    path('feedback1/', views.feedback, name='feedback1')

]