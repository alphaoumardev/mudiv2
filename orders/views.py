from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django_countries import countries
from rest_framework.templatetags.rest_framework import data
from rest_framework.views import APIView

# from mart.serializers import *
from orders.models import *
from orders.serializers import CartItemSerializer, OrderSerializer, OrderItemMiniSerializer, CartItemUpdateSerializer, \
    CartItemMiniSerializer


class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        user = request.user
        address = ShippingAddress.objects.filter(user=user, primary=True).first()
        product = get_object_or_404(Product, pk=pk)
        if product.stock == 0:
            return Response("This product is out of stock")
        try:
            order_reference = request.data.get("order_reference", '')
            quantity = request.data.get("quantity", 1)

            total = quantity * product.price
            order = Order().create_order(user, order_reference, status, address, checked_out=True,
                                         isPaid=False, isDelivered=False,
                                         paid_at=datetime.datetime.now(),
                                         delivered_at=datetime.datetime.now(),
                                         ordered_at=datetime.datetime.now(),
                                         refund_requested=False,
                                         isReceived=False,
                                         isRefunded=False, )
            order_item = OrderItem().create_orderItem(order, product, quantity, total)
            serializer = OrderItemMiniSerializer(order_item, )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response("An error occur when creating the order", e)


class CreateCartApiView(ListCreateAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = CartItem.objects.filter(cart__user=user, )
        return queryset

    # def create(self, request, *args, **kwargs):
    #     user = request.user
    #     # cart = get_object_or_404(Cart, user=user)
    #     product = get_object_or_404(Product, pk=request.data['product'])
    #     color = get_object_or_404(CartItem, pk=request.data['color'])
    #     size = get_object_or_404(CartItem, pk=request.data['size'])
    #
    #     # current_item = CartItem.objects.filter(cart=cart, product=product)
    #     quantity = int(request.data['quantity'])
    #
    #     # if current_item.count() > 0:
    #     #     Response("You already have this product in your cart")
    #
    #     if quantity > product.stock:
    #         return Response("There is no enough product in stock")
    #     # seriliazer = CartItemSerializer(data=request.data)
    #     cartItem = CartItem(cart=cart, product=product, quantity=quantity, color=color, size=size)
    #     # product.stock -= cartItem.quantity
    #     # cartItem.save()
    #     serializer = CartItemSerializer(cartItem)
    #     # if serializer.is_valid():
    #     serializer.save()
    #         # return Response(serializer.data)
    #     total = float(product.price) * quantity
    #     cart.total = total
    #     cart.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


class CartItemView(RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

    def retrieve(self, request, *args, **kwargs):
        cartItem = self.get_object()
        if cartItem.user != request.user:
            raise PermissionDenied("Access Denied")
        serializer = self.get_serializer(cartItem)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        cartItem = self.get_object()
        product = get_object_or_404(Product, pk=request.data['product'])

        if cartItem.user != request.user:
            raise PermissionDenied("This cart don't belong to you")

        quantity = int(request.data['quantity'])

        if quantity > product.stock:
            return Response("This product is out of stock")
        total = float(product.price) * quantity
        cartItem.total = total
        cartItem.user = request.user
        cartItem.save()
        serializer = CartItemUpdateSerializer(cartItem, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        cartItem = self.get_object()
        if cartItem.user != request.user:
            raise PermissionDenied("Access Denied")
        cartItem.delete()
        return Response("You have successfully deleted your cart item", status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def create_cart(request):
    user = request.user
    if request.method == 'GET':
        items = CartItem.objects.filter(user=user, )
        serializer = CartItemMiniSerializer(items, many=True)
        return Response(serializer.data)

    if request.method == "POST":

        seriliazer = CartItemSerializer(data=request.data, many=False)

        if seriliazer.is_valid():
            seriliazer.save()

            product = Product.objects.get(id=request.data['product'])
            quantity = int(request.data['quantity'])
            cartItem = get_object_or_404(CartItem, product=product)

            total = float(product.price) * quantity
            cartItem.total = total
            cartItem.user = request.user
            cartItem.save()
            print(total, cartItem.user)
            print(request.data)
            return Response(seriliazer.data)
        return Response(seriliazer.errors)


@api_view(["GET", "POST"])
# @permission_classes([AllowAny])
def cart(request):
    user = request.user
    # product = get_object_or_404(Product, id=request.data['product'])
    # product = Product.objects.get(id=request.data['product'])
    if request.method == 'GET':
        items = CartItem.objects.filter(user=user, )
        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data)

    if request.method == "POST":

        seriliazer = CartItemSerializer(data=request.data, many=False)

        if seriliazer.is_valid():
            seriliazer.save()

            product = Product.objects.get(id=request.data['product'])
            quantity = int(request.data['quantity'])
            cartItem = get_object_or_404(CartItem, user=user)

            total = float(product.price) * quantity
            cartItem.total = total
            # cartItem.user = request.user
            cartItem.save()
            print(total, cartItem.user)
            print(request.data)
            return Response({"data": seriliazer.data, "total": total})
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
        # ShippingAddress.objects.create(
        #     order=order,
        #     user=user,
        #     state=data['shippingAddress']['state'],
        #     address=data['shippingAddress']['address'],
        #     city=['shippingAddress']['city'],
        #     zip=['shippingAddress']['zip'],
        #     country=['shippingAddress']['country'],
        #     street=['shippingAddress']['street']
        # )

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
    except Exception as e:
        return Response(f'Order does not exist {e}', status=status.HTTP_400_BAD_REQUEST)
    # finally:
    #     return Response("This order does not exist")


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
