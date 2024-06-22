from django.urls import path
from booking import views
urlpatterns=[
    path('reg/(?P<idd>\w+)',views.register,name='booking'),
    path('view/',views.view),
    path('book/(?P<idd>\w+)', views.book, name='book'),
    path('manage/',views.manage),
    path('viewstatus/',views.viewstaus),
    path('accept/(?P<idd>\w+)', views.accept, name='approve'),
    path('reject/(?P<idd>\w+)', views.reject, name='decline'),
    # url('viewfood/', views.viewfood),
    # url('books/(?P<ee>\w+)', views.bookf, name='bo'),
]