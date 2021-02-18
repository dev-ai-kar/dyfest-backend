from django.urls import path
from base.views import event_views as views

urlpatterns = [
    path('', views.getEvents, name="events"),
    path('<str:pk>/', views.getEvent, name="event"),
]