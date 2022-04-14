from django.db import models
from mart.models import Product
# from customer.models import UserAccount
from accounts.models import UserAccount
from django.contrib.auth.models import User, AbstractUser
import uuid


class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItems(models.Model):
    order_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantitty = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderDetails(models.Model):
    details_id = models.OneToOneField(OrderItems, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    total = models.IntegerField(null=True)
    payment_id = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PaymentDetails(models.Model):
    payment_id = models.OneToOneField(OrderDetails, primary_key=True, on_delete=models.CASCADE)
    order_id = models.UUIDField(default=uuid.uuid4, editable=False)
    total_amount = models.DecimalField(decimal_places=3, max_digits=6, null=True)
    provider = models.CharField(max_length=20)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.provider


class UserPay(models.Model):
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=20)
    provider = models.CharField(max_length=20)
    account_no = models.UUIDField()
    expired_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.payment_type + self.provider
