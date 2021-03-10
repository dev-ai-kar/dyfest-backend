from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.models import Event, Order, OrderItem, ShippingAddress
from base.serializer import EventSerializer, OrderSerializer


from rest_framework import status

@api_view(['POST'])
@permission_classes(['isAuthenticated'])
def addOrderItems(request):
    user = request.user
    data = request.data

    orderItems = data['orderItems']
    if orderItems and len(orderItems) == 0:
        return Response({'detail':'No Order Items'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        # (1) Create order
        order= Order.objects.create(
            user=user,
            paymentMethod=data['paymentMethod'],
            taxPrice=data['taxPrice'],
            shippingPrice=data['shippingPrice'],
            totalPrice=data['totalPrice']
            )
        # (2) Create ShippingAddress
        shipping = ShippingAddress.Objects.create(
            order = order,
            address = data['shippingAddress']['address'],
            city = data['shippingAddress']['city'],
            postalCode = data['shippingAddress']['postalCode'],
            country = data['shippingAddress']['country'],
            # shippingPrice 
        )
        # (3) Create Order Items adn set order to orderItems relationship
        for i in orderItems:
            event = Event.objects.get(_id=i['event'])
            item = OrderItem.objects.create(
                event = event,
                order = order,
                name = event.name,
                qty = i['qty'],
                price = i['price'],
                image = event.image.url,
            )
        # (4)Update stock
        event.countInStock -= item.qty
        event.save()
    serializer = OrderSerializer(order, many= True)
    return Response(serializer.data)