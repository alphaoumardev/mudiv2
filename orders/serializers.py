from .models import *

class WishListModel(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'


# The shopping start here
class CartItemModel(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class OrderDetailsModel(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'


class PaymentDetailsModel(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = '__all__'


class UserPayModel(serializers.ModelSerializer):
    class Meta:
        model = UserPay
        fields = '__all__'
