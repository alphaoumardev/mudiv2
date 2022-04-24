import uuid

from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django_countries.fields import CountryField

from accounts.models import UserAccount
from mart.models import Product, Variant
from mudi import settings


class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)


class Order(models.Model):
    # item = models.ManyToManyField("CartItem")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reference_code = models.UUIDField(default=uuid.uuid4(), blank=False, null=False)

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
    # def get_total(self):
    #     total = 0
    #     for products in self.product.all():
    #         total += products.get_final_price()
    #     if self.coupon:
    #         total -= self.coupon.amount
    #     return total


class CartItem(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    # variations = models.ManyToManyField(Variant)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)

    quantity = models.IntegerField(null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_total_item_price(self):
        return self.quantity * self.product.price

    def get_total_discount_price(self):
        return self.quantity * self.product.discount

    def get_coupon_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_price()

    def get_final_price(self):
        if self.product.discount:
            return self.get_total_discount_price()
        return self.get_total_item_price()


class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    country = CountryField(multiple=False)
    state = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=20, null=True)
    street = models.CharField(max_length=100, null=True)
    zip = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=200, null=True)

    default = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Addresses'


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


