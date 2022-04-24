from accounts.serializers import UserCreateSerializer
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
    # variants = serializers.SerializerMethodField()
    # product = serializers.SerializerMethodField()
    # final_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = '__all__'

    def get_products(self, obj):
        return ProductsModel(obj.product).data

    def get_item_variants(self, obj):
        return VariantModel(obj.variants.all(), many=True).data

    def get_fianl_price(self, obj):
        return obj.get_final_price()


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    shippingAddress = serializers.SerializerMethodField(read_only=True)
    cartItems = serializers.SerializerMethodField(read_only=True)
    # total = serializers.SerializerMethodField()
    # coupon = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'
        # fields = ['reference_code', 'total', 'coupon', 'cart_items',
        #           'checked_out', 'shipping_address', 'payment',
        #           'delivered', 'received', 'refunf_requested', 'refunded',
        #           'ordered_at', 'updated_at']

    def get_cartItems(self, obj):
        items = obj.cartitem_set.all()
        serializer = CartItemSerializer(items, many=True)
        return serializer.data
        # return CartItemSerializer(obj.product.all(), many=True).data

    def get_shippingAddress(self, obj):
        try:
            address = ShippingAddressSerializer(obj.shippingAddress, many=False).data
        except:
            address = False
        return address

    def get_user(self, obj):
        items = obj.user
        return UserCreateSerializer(items, many=False).data

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
    # country = CountryField()

    class Meta:
        model = ShippingAddress
        fields = '__all__'
        # fields = ['user', 'street_address', 'apartment_address',
        #           'country', 'zip', 'address_type', 'default']


class RefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refund
        fields = '__all__'
