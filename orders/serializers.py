from mart.serializers import ProductsModel, VariantModel
from .models import *
from rest_framework import serializers


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'


# The shopping start here
class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['code', 'amound', 'create_at', 'expired_at']


class CartItemSerializer(serializers.ModelSerializer):
    variants = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()
    final_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['variants', 'product', 'quantity', ]

    def get_products(self, obj):
        return ProductsModel(obj.product).data

    def get_item_variants(self, obj):
        return VariantModel(obj.variants.all(), many=True).data

    def get_fianl_price(self, obj):
        return obj.get_final_price()


class OrderSerializer(serializers.ModelSerializer):
    cart_items = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()
    coupon = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['reference_code', 'total', 'coupon', 'cart_items',
                  'checked_out', 'shipping_address', 'payment',
                  'delivered', 'received', 'refunf_requested', 'refunded',
                  'ordered_at', 'updated_at']

    def get_cart_items(self, obj):
        return CartItemSerializer(obj.product.all(), many=True).data

    def get_total(self, obj):
        return obj.get_total()

    def get_coupon(self, obj):
        if obj.coupon is not None:
            return CouponSerializer(obj.coupon).data


class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class ShippingAddressSerializer(serializers.ModelSerializer):
    country = CountryField()

    class Meta:
        model = ShippingAddress
        fields = ['user', 'street_address', 'apartment_address',
                  'country', 'zip', 'address_type', 'default']


class RefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refund
        fields = '__all__'
