import uuid

from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django_countries.fields import CountryField

from accounts.models import UserAccount
from mart.models import Product, Variant
from mudi import settings


class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)


class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variant)
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


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(CartItem)
    reference_code = models.UUIDField(default=uuid.uuid4(), blank=False, null=False)

    checked_out = models.BooleanField(default=False)
    shipping_address = models.ForeignKey("ShippingAddress", on_delete=models.SET_NULL, null=True, blank=True)
    payment = models.ForeignKey("Payments", on_delete=models.SET_NULL, null=True, blank=True)
    coupon = models.ForeignKey("Coupon", on_delete=models.SET_NULL, null=True, blank=True)
    delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refunded = models.BooleanField(default=False)
    ordered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name

    def get_total(self):
        total = 0
        for products in self.products.all():
            total += products.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total


ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)


class ShippingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name_plural = 'Addresses'


class Payments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    payment_id = models.CharField(max_length=50, null=True, blank=True)
    order_id = models.UUIDField(default=uuid.uuid4, editable=False)
    total_amount = models.DecimalField(decimal_places=3, max_digits=6, null=True)
    provider = models.CharField(max_length=20, null=True)
    paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.provider


class Coupon(models.Model):
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


