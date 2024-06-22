from django.urls import path
from order import views
urlpatterns=[
    path('reg/(?P<idd>\w+)',views.register,name='boo'),
    path('view/',views.view),
    path('book/(?P<idd>\w+)', views.book, name='book'),
    path('manage/',views.manage),
    path('viewstatus/',views.viewstaus),
    path('accept/(?P<idd>\w+)', views.accept, name='approve2'),
    path('reject/(?P<idd>\w+)', views.reject, name='decline3'),
]