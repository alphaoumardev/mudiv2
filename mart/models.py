from django.db import models
from django.contrib.auth.models import User, AbstractUser
# from orders.models import CartItem, OrderItems
# from customer.models import UserAccount
from accounts.models import UserAccount
import uuid


class Genre(models.Model):
    genre_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.genre_name


class Types(models.Model):
    type_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.type_name


class Category(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=False)
    type = models.ForeignKey(Types, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.genre.genre_name + " >  " + self.type.type_name


class Product(models.Model):
    SALES = (
        ("Sale", "Sale"),
        ("New", "New"),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    sku = models.UUIDField(default=uuid.uuid4(), blank=False, null=False)
    brand = models.CharField(max_length=20, null=True)
    description = models.TextField(max_length=400, blank=False)
    price = models.DecimalField(default=20, decimal_places=2, max_digits=6)

    image = models.ImageField(upload_to="mudi", null=True, blank=False)
    image_hover = models.ImageField(upload_to="mudi", null=True, blank=True)

    status = models.BooleanField(default=True, null=True, )
    rating = models.IntegerField(default=1)
    stock = models.IntegerField(default=50)
    quantity = models.IntegerField(default=1)
    onsale = models.CharField(null=True, blank=True, choices=SALES, max_length=10)
    discount = models.DecimalField(decimal_places=2, max_digits=3, default=1, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    def image_preview(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" style="width: 50px; height:50px; object-fit:contain;" />')
        else:
            return 'No image found'

    image_preview.short_description = "Image"

    def __str__(self):
        return self.name


class FuturedImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    image_url = models.ImageField(upload_to="mudi", blank=True, null=True)

    def __str__(self):
        return self.image_url.url


class Tags(models.Model):
    tag_name = models.CharField(blank=True, null=True, max_length=15, unique=True)

    def __str__(self):
        return self.tag_name


class ColorsOption(models.Model):
    color_name = models.CharField(blank=True, null=True, max_length=15, unique=True)

    def __str__(self):
        return self.color_name


class SizesOption(models.Model):
    size_name = models.CharField(blank=True, null=True, max_length=15, unique=True)

    def __str__(self):
        return self.size_name


class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(ColorsOption, on_delete=models.CASCADE, blank=True, null=True)
    size = models.ForeignKey(SizesOption, on_delete=models.CASCADE, blank=True, null=True)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE, blank=True, null=True)


class Sliders(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)


class Comments(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    content = models.TextField(max_length=400)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject + "  " + self.content
