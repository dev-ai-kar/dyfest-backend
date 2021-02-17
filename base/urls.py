from django.urls import path
from . import views

urlpatterns = [
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', views.getRoutes, name= "routes"),
    path('events/', views.getEvents, name="events"),
    path('events/<str:pk>/', views.getEvent, name="event"),
]