import datetime
import uuid

from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

from accounts.models import UserAccount
from mart.models import Product, Variant
from mudi import settings


class Wishlist(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True, blank=False, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)


class ShippingAddress(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True, blank=False, null=False)
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE, null=True, blank=True)
    country = CountryField(multiple=False)
    state = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=20, null=True)
    district = models.CharField(max_length=100, null=True)
    street = models.CharField(max_length=100, null=True)
    zip = models.CharField(max_length=10, null=True)
    details = models.CharField(max_length=200, null=True)

    primary = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Addresses'


# class Cart(models.Model):
#     user = models.OneToOneField(UserAccount, on_delete=models.CASCADE, null=True)
#     total = models.DecimalField(decimal_places=2, max_digits=6, null=True, )


# @receiver(post_save, sender=UserAccount)
# def create_user_cart(self, sender, created, instance, *args, **kwargs):
#     if created:
#         Cart.objects.create(user=instance)
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)


class CartItem(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    total = models.DecimalField(decimal_places=2, max_digits=6, null=True, )
    quantity = models.IntegerField(default=1)
    color = models.CharField(max_length=20, null=True)
    size = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.product.name


class Order(models.Model):
    PENDING = "pending"
    COMPLETED = "Completed"
    ORDER_STATUS = ((PENDING, 'pending'), (COMPLETED, 'completed'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_reference = models.UUIDField(default=uuid.uuid4(), blank=False, null=False)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default=PENDING)
    address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE, null=True)
    checked_out = models.BooleanField(default=False)
    isPaid = models.BooleanField(default=False)

    isDelivered = models.BooleanField(default=False)
    delivered_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isReceived = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    isRefunded = models.BooleanField(default=False)
    ordered_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.user.first_name

    @staticmethod
    def create_order(user, order_reference, status, address,
                     paid_at,
                     checked_out=False,
                     isPaid=False, isDelivered=False,
                     delivered_at=datetime.datetime.now(),
                     ordered_at=datetime.datetime.now(),
                     refund_requested=False,
                     isReceived=False, isRefunded=False, ):
        order = Order()
        order.user = user,
        order.order_reference = order_reference
        order.status = status,
        order.address = address,
        order.checked_out = checked_out,
        order.paid_at = paid_at,
        order.isPaid = isPaid,
        order.isDelivered = isDelivered,
        order.delivered_at = delivered_at,
        order.ordered_at = ordered_at,
        order.refund_requested = refund_requested,
        order.isReceived = isReceived,
        order.isRefunded = isRefunded
        order.save()
        return order
    # def get_total(self):
    #     total = 0
    #     for products in self.product.all():
    #         total += products.get_final_price()
    #     if self.coupon:
    #         total -= self.coupon.amount
    #     return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(null=True)
    total = models.DecimalField(decimal_places=2, max_digits=6)

    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def get_total_orderitem_price(self):
    #     return self.quantity * self.product.price

    # def get_total_discount_price(self):
    #     return self.quantity * self.product.discount
    #
    # def get_coupon_amount_saved(self):
    #     return self.get_total_item_price() - self.get_total_discount_price()
    #
    # def get_final_price(self):
    #     if self.product.discount:
    #         return self.get_total_discount_price()
    #     return self.get_total_item_price()
    @staticmethod
    def create_orderItem(product, order, quantity, total,):
        order_item = OrderItem()
        order_item.order = order,
        order_item.product = product,
        order_item.quantity = quantity,
        order_item.total = total
        order_item.save()
        return order_item


class Payments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    payment_id = models.CharField(max_length=50, null=True, blank=True)
    total_amount = models.DecimalField(decimal_places=3, max_digits=6, null=True)
    provider = models.CharField(max_length=20, null=True)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.provider


class Coupon(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField(max_length=15)
    amount = models.FloatField()
    added_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()
