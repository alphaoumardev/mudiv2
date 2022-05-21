from accounts.serializers import UserCreateSerializer
from mart.serializers import ProductSerializer
from .models import *
from rest_framework import serializers


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class ShippingAddressReadSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer(read_only=True)

    class Meta:
        model = ShippingAddress
        fields = ['id', 'user', 'country', 'state', 'city', 'street', 'details', 'zip', 'order_note']


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'


class WishlistReadSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=False, read_only=True)
    user = UserCreateSerializer(required=False, read_only=True)

    class Meta:
        model = Wishlist
        fields = ['id', 'product', 'user']


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['code', 'amound', 'create_at', 'expired_at']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class CartItemReadSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True,)
    user = UserCreateSerializer(read_only=True,)

    class Meta:
        model = CartItem
        fields = ["id", 'product', 'quantity', 'color', 'size', 'user', "total"]


class CartItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'color', 'size']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemReadSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = OrderItem
        fields = ["id", 'product', 'quantity', 'color', 'size', "total"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderReadSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer(required=False, read_only=True)
    address = ShippingAddressReadSerializer(required=False, read_only=True)
    cart = CartItemReadSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['status', 'checked_out', 'isPaid', 'isRefunded', 'isDelivered',
                  'refund_requested', 'order_reference',  'paid_at',
                  'user', 'address', 'cart', 'amount']


class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class RefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refund
        fields = '__all__'
