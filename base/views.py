from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .products import products

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
    return Response(products)

@api_view(['GET'])
def getEvent(request, pk):
    product = None
    for i in products:
        if i['_id'] == pk:
            product = i
            break
    return Response(product)