from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Wishlist)
admin.site.register(OrderItems)
admin.site.register(CartItem)
admin.site.register(OrderDetails)
admin.site.register(PaymentDetails)
admin.site.register(UserPay)
