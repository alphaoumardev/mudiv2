from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django_countries import countries
from rest_framework.views import APIView

# from mart.serializers import *
from orders.models import *
from orders.serializers import CartItemSerializer, OrderSerializer


@api_view(["GET", "POST", "DELETE"])
def get_cart(request):
    if request.method == 'GET':
        items = CartItem.objects.all()
        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        seriliazer = CartItemSerializer(data=request.data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response(seriliazer.data)
        return Response(seriliazer.errors)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_countries(request, *args, **kwargs):
    return Response(countries, status=HTTP_200_OK)


# Create your views here.
class CartItemViews(APIView):
    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({serializer.data}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk:
            item = CartItem.objects.get(id=pk)
            serializer = CartItemSerializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)

        item = CartItem.objects.all()
        serializer = CartItemSerializer(item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk=None):
        item = CartItem.objects.get(id=pk)
        serializer = CartItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({serializer.data})
        else:
            return Response(serializer.errors)

    def delete(self, request, pk=None):
        item = get_object_or_404(CartItem, pk=pk)
        item.delete()
        return Response({"Item Deleted"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_order_items(request):
    user = request.user
    data = request.data
    cartItems = data['cartItems']
    if cartItems and len(cartItems) == 0:
        return Response('No order items', status=status.HTTP_400_BAD_REQUEST)
    else:
        order = Order.objects.create(
            user=user,
        )
        ShippingAddress.objects.create(
            order=order,
            user=user,
            state=data['shippingAddress']['state'],
            address=data['shippingAddress']['address'],
            city=['shippingAddress']['city'],
            zip=['shippingAddress']['zip'],
            country=['shippingAddress']['country'],
            street=['shippingAddress']['street']
        )

        for i in cartItems:
            product = Product.objects.get(id=i['product'])
            item = CartItem.objects.create(
                product=product,
                order=order,
                quantity=i['quantity'],
                price=i['price'],
            )
            product.stock -= item.quantity
            product.save()

        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_my_orders(request):
    user = request.user
    orders = user.order_set.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])  # just the admin can monitor the whole orders
def get_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_order_by_id(request, pk):
    user = request.user
    try:
        order = Order.objects.get(id=pk)
        if user.is_staff or order.user == user:
            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data)
        else:
            return Response('Not authorized to view this order', status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response('Order does not exist', status=status.HTTP_400_BAD_REQUEST)
    finally:
        return Response("This order does not exist")


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_order_to_paid(request, pk):
    order = Order.objects.get(id=pk)
    order.isPaid = True
    order.paid_at = datetime.now()
    order.save()
    return Response('Order was paid')


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_order_to_delivered(request, pk):
    order = Order.objects.get(id=pk)
    order.isDelivered = True
    order.delivered_at = datetime.now()
    order.save()
    return Response('Order was delivered')
