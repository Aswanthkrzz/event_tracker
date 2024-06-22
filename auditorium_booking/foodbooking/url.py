from django.urls import path
from foodbooking import views
urlpatterns=[
    path('foo1/(?P<idd>\w+)',views.food,name='foo1'),
    path('accepty/(?P<idd>\w+)', views.accepty, name='approvey'),
    path('rejecty/(?P<idd>\w+)', views.rejecty, name='decliney'),
    path('view/',views.manage),
    path('status/',views.status),
]