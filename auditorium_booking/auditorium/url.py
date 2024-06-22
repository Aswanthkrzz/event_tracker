from django.urls import path
from auditorium import views
urlpatterns=[
    path('reg/',views.register),
    path('search/',views.search),
    path('view/',views.viewsearch),
    path('updp/',views.updprof),
    path('vblock/',views.vblock),
    path('upd/(?P<idd>\w+)',views.update,name='up'),
    path('delet/(?P<idd>\w+)',views.delete,name='delet'),
    path('update/(?P<idd>\w+)',views.accepted,name='acp'),
    path('reject/(?P<idd>\w+)',views.rejected,name='rejecty'),
    path('delete1/(?P<idd>\w+)', views.delete1, name='delet1'),
    path('block/(?P<idd>\w+)', views.block, name='block'),
    path('auditorium_details/(?P<id>\w+)',views.auditorium_details, name = 'auditorium_details'),
    path('feedback/(?P<id>\w+)',views.add_feedback,name='auditorium_feedback'),
    path('feedback1/',views.feedback1,name='feedback1')

]