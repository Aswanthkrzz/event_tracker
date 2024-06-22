from django.urls import path
from food import views
urlpatterns=[
    path('dec/',views.post),
    path('view/',views.view),
]