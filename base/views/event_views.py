from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.models import Event
from base.serializer import EventSerializer


from rest_framework import status


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