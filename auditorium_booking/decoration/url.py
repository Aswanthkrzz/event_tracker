from django.urls import path
from decoration import views
urlpatterns=[
    path('dec/',views.post),
    path('view/',views.view),
]