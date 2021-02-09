from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Event
from .products import products
from .serializer import EventSerializer
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
      '/api/events/',
      '/api/events/create/',

      '/api/events/upload/',

      '/api/events/<id>/reviews/',

      '/api/events/top/',
      '/api/events/<id>/',

      '/api/events/delete/<id>/',
      '/api/events/<update>/<id>/',
    ]
    return Response(routes)

@api_view(['GET'])
def getEvents(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many= True) # many = True # serializing many object or one
    return Response(serializer.data)

@api_view(['GET'])
def getEvent(request, pk):
    event = Event.objects.get(_id=pk)
    serializer = EventSerializer(event, many= False) # many = True # serializing many object or one
    return Response(serializer.data)