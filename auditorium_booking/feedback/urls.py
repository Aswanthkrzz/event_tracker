from django.urls import path
from feedback import views
urlpatterns=[
    path('feedback/',views.feedback),
    path('view/', views.viewfeed),
    path('view1/', views.viewfeed1),
    path('view2/', views.viewfeed2),

]