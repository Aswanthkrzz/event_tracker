from django.urls import path
from event import views

urlpatterns = [
    path('event/',views.event),
    path('serch/',views.search)
]