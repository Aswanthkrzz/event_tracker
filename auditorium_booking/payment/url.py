# from django.conf.urls import url
# from payment import views
# urlpatterns=[
#     url('PAY/(?P<idd>\w+)',views.payment,name='pay')
#
# ]
from django.urls import path
from payment import views
urlpatterns=[
    path("", views.order_payment, name="payment"),
    # path("callback/", views.callback, name="callback"),
    # path("hello/", views.hello, name="hello"),

]