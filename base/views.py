from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Event
from .products import products
from .serializer import EventSerializer, UserSerializer, UserSerializerWithToken

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # data can be send in the JWT TOKEN ITSELF ref: https://github.com/SimpleJWT/django-rest-framework-simplejwt/blob/a0c75415cdcc39cce19a09c6acec54f298076704/rest_framework_simplejwt/serializers.py#L58
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data

        for k,v in serializer.items():
            data[k] = v

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


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
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many= False)
    return Response(serializer.data)

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