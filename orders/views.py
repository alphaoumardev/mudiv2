from mart.models import Review
from orders.models import *
from datetime import datetime
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from orders.serializers import CartItemSerializer, OrderSerializer, CartItemUpdateSerializer, \
    WishlistSerializer, WishlistReadSerializer, ShippingAddressSerializer, OrderReadSerializer, \
    CartItemReadSerializer, OrderItemReadSerializer, ShippingAddressReadSerializer, OrderItemSerializer, \
    ReviewSerializer


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
        product.stock -= quantity
        product.save()
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
    order_total = 0.0

    if request.method == 'GET':
        cartItems = CartItem.objects.filter(paid=False, user=user,).order_by('-id')
        cart_count = cartItems.count()
        serializer = CartItemReadSerializer(cartItems, many=True)

        for item in cartItems:
            if item is not None:
                order_total += float(item.total)


        return Response(
            {
                "result": serializer.data,
                "order_total": order_total,
                "cart_count": cart_count,
            })

    if request.method == "POST":

        serializer = CartItemSerializer(data=request.data, many=False)

        product = Product.objects.get(id=request.data['product'])
        checkItem = CartItem.objects.filter(product_id=product, paid=False).exists()

        if checkItem:
            update_data = CartItem.objects.get(product_id=product, )
            serializer = CartItemSerializer(instance=update_data, data=request.data, many=False)

            if serializer.is_valid():
                serializer.save()

                product = Product.objects.get(id=request.data['product'])
                quantity = int(request.data['quantity'])
                cartItem = get_object_or_404(CartItem, product=product, paid=False)

                product.stock -= quantity
                product.save()
                cartItem.total = float(product.price) * quantity
                cartItem.user = request.user
                cartItem.save()
                return Response(serializer.data)
            return Response(serializer.errors)

        if serializer.is_valid():
            serializer.save()

            product = Product.objects.get(id=request.data['product'])
            quantity = int(request.data['quantity'])
            cartItem = get_object_or_404(CartItem, product=product, paid=False)

            product.stock -= quantity
            product.save()
            cartItem.total = float(product.price) * quantity
            cartItem.user = request.user
            cartItem.save()
            return Response(serializer.data)
        return Response(serializer.errors,)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def create_wishlist(request, ):
    user = request.user
    if request.method == 'GET':
        wishlist = Wishlist.objects.filter(user=user).order_by('-id')
        wishlist_count = wishlist.count()
        serializer = WishlistReadSerializer(wishlist, many=True)
        return Response({"result": serializer.data, "wishlist_count": wishlist_count, })

    if request.method == "POST":
        serializer = WishlistSerializer(data=request.data, many=False, )

        product = Product.objects.get(id=request.data['product'])
        checkItem = Wishlist.objects.filter(product_id=product).exists()

        if checkItem:
            updated_data = Wishlist.objects.get(product_id=product)
            serializer = WishlistSerializer(instance=updated_data, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def operate_wishlist(request, pk):
    user = request.user
    if request.method == 'GET':
        wishlist = Wishlist.objects.get(id=pk, user=user)
        serializer = WishlistReadSerializer(wishlist, many=False)
        # checkItem = Wishlist.objects.filter(product_id=product).exists()

        return Response(serializer.data)

    if request.method == 'PUT':
        wishlist_item = Wishlist.objects.get(id=pk)
        serializer = WishlistSerializer(instance=wishlist_item, data=request.data, )
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    if request.method == 'DELETE':
        wishlist_item = Wishlist.objects.get(id=pk)
        wishlist_item.delete()
        return Response("The wishlist item is deleted")


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def create_address(request, ):
    user = request.user
    if request.method == 'GET':
        shipping_address = ShippingAddress.objects.filter(user=user).first()
        serializer = ShippingAddressReadSerializer(shipping_address, many=False)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ShippingAddressSerializer(data=request.data, many=False, )

        user_address = UserAccount.objects.get(id=request.data['user'])
        checkAddress = ShippingAddress.objects.filter(user_id=user_address).exists()

        if checkAddress:
            updated_address = ShippingAddress.objects.get(user_id=user_address)
            serializer = ShippingAddressSerializer(instance=updated_address, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_orderItems(request, ):
    user = request.user
    if request.method == 'GET':
        orderItem = OrderItem.objects.filter(user=user).order_by('-id')
        serializer = OrderItemReadSerializer(orderItem, many=True)
        return Response(serializer.data)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def create_order(request, ):
    user = request.user
    if request.method == 'GET':
        orders = Order.objects.filter(user=user)
        serializer = OrderReadSerializer(orders, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = OrderSerializer(data=request.data, many=False, )

        if serializer.is_valid():
            serializer.save()

            carts = CartItem.objects.filter(user=user, paid=False)
            order = Order.objects.filter(user=user).last()
            for p in carts:
                p.paid = True
                p.save()
            order.status = "COMPLETED"
            order.checked_out = True
            order.isPaid = True
            order.cart.set(carts)
            order.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def create_orderItem(request, pk):
    if request.method == 'GET':
        # The orderItem
        orderItems = OrderItem.objects.filter(order=pk)
        orders_total = 0
        for item in orderItems:
            orders_total += item.total
        serializer = OrderItemReadSerializer(orderItems, many=True)
        return Response(
            {
                "result": serializer.data,
                "orders_total": orders_total,
            })

    if request.method == "POST":
        user = request.user
        serializer = OrderItemSerializer(data=request.data, many=False)

        if serializer.is_valid():
            serializer.save()

            order_products = CartItem.objects.filter(user=user)

            orderItem = OrderItem.objects.get(order=pk)
            orderItem.product.set(order_products)


            # product = Product.objects.get(id=request.data['product'])
            # quantity = int(request.data['quantity'])
            # orderItem = get_object_or_404(OrderItem, product=product)
            # orderItem.total=
            # product.stock -= quantity
            # product.save()
            # total = float(product.price) * quantity

            # orderItem.total = total
            orderItem.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_my_orders(request):
    user = request.user
    orders = user.order_set.all()
    serializer = OrderReadSerializer(orders, many=True)
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


class CreateCartApiView(ListCreateAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = CartItem.objects.filter(cart__user=user, )
        return queryset

    def create(self, request, *args, **kwargs):
        user = request.user
        cart = get_object_or_404(CartItem, user=user)
        product = get_object_or_404(Product, pk=request.data['product'])
        color = get_object_or_404(CartItem, pk=request.data['color'])
        size = get_object_or_404(CartItem, pk=request.data['size'])

        # current_item = CartItem.objects.filter(cart=cart, product=product)
        quantity = int(request.data['quantity'])

        # if current_item.count() > 0:
        #     Response("You already have this product in your cart")

        if quantity > product.stock:
            return Response("There is no enough product in stock")
        # serializer = CartItemSerializer(data=request.data)
        cartItem = CartItem(cart=cart, product=product, quantity=quantity, color=color, size=size)
        # product.stock -= cartItem.quantity
        # cartItem.save()
        serializer = CartItemSerializer(cartItem)
        # if serializer.is_valid():
        serializer.save()
        # return Response(serializer.data)
        total = float(product.price) * quantity
        cart.total = total
        cart.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# class OrderView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request, pk, *args, **kwargs):
#         user = request.user
#         address = ShippingAddress.objects.filter(user=user, primary=True).first()
#         product = get_object_or_404(Product, pk=pk)
#         if product.stock == 0:
#             return Response("This product is out of stock")
#         try:
#             order_reference = request.data.get("order_reference", '')
#             quantity = request.data.get("quantity", 1)
#
#             total = quantity * product.price
#             order = Order().create_order(user, order_reference, status, address, checked_out=True,
#                                          isPaid=False, isDelivered=False,
#                                          paid_at=datetime.datetime.now(),
#                                          delivered_at=datetime.datetime.now(),
#                                          ordered_at=datetime.datetime.now(),
#                                          refund_requested=False,
#                                          isReceived=False,
#                                          isRefunded=False, )
#             order_item = OrderItem().create_orderItem(order, product, quantity, total)
#             # serializer = OrderItemReadSerializer(order_item, )
#
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         except Exception as e:
#             return Response("An error occur when creating the order", e)
