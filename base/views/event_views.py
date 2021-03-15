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

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createEvent(request):
    user=request.user
    event = Event.objects.create(
        user=user, 
        name = 'Sample Name',
        price = 0,
        brand = 'Sample Brand',
        countInStock = 0,
        category ='Sample Category',
        description = 'Sample Description'
    )
    serializer = EventSerializer(event, many= False) # many = True # serializing many object or one
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def updateEvent(request, pk):
    data = request.data
    event = Event.objects.get(_id = pk)
    event.name = data['name']
    event.brand = data['brand']
    event.category = data['category']
    event.countInStock = data['countInStock']
    event.description = data['description']

    event.save()

    serializer = EventSerializer(event, many= False) # many = True # serializing many object or one
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteEvent(request, pk):
    event = Event.objects.get(_id=pk)
    event.delete()
    return Response('Event Deleted')