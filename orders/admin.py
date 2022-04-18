from django.contrib import admin
from .models import *


admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(CartItem)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(Payments)
admin.site.register(ShippingAddress)
