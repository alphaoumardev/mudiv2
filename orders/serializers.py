from accounts.serializers import UserCreateSerializer
from mart.serializers import ProductSerializer, VariantSerializer
from .models import *
from rest_framework import serializers
from mart.models import Product, Variant


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'


# The shopping start here
# class CartProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['code', 'amound', 'create_at', 'expired_at']


# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cart
#         fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class CartItemMiniSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=False, many=False)
    user = UserCreateSerializer(read_only=False, many=False)

    class Meta:
        model = CartItem
        fields = ["id", 'product', 'quantity', 'color', 'size', 'user', "total"]


class CartItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'color', 'size']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderMiniSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer(required=False)
    address = ShippingAddressSerializer(required=False)

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemMiniSerializer(serializers.ModelSerializer):
    order = OrderMiniSerializer(read_only=True, required=False)
    product = ProductSerializer(read_only=True, required=False)

    class Meta:
        model = OrderItem
        fields = '__all__'


class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class RefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refund
        fields = '__all__'

# class OrderSerializer(serializers.ModelSerializer):
#     # user = serializers.SerializerMethodField(read_only=True)
#     # shippingAddress = serializers.SerializerMethodField(read_only=True)
#     # cartItems = serializers.SerializerMethodField(read_only=True)
#
#     # total = serializers.SerializerMethodField()
#     # coupon = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Order
#         fields = '__all__'
#         # fields = ['reference_code', 'total', 'coupon', 'cart_items',
#         #           'checked_out', 'shipping_address', 'payment',
#         #           'delivered', 'received', 'refunf_requested', 'refunded',
#         #           'ordered_at', 'updated_at']
