# Register your models here.
from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', "brand", "category", "stock", "price", "image_preview")


# Register your models here.
class Variants(admin.TabularInline):
    model = Variant


class FuturedImg(admin.TabularInline):
    model = FuturedImages


class ProductAdmins(admin.ModelAdmin):
    inlines = [Variants, FuturedImg]
    # list_display = ['color_name']


admin.site.register(Genre)
admin.site.register(Types)
admin.site.register(Category)
admin.site.register(Product, ProductAdmins)  # ProductAdims
admin.site.register(Tags)
admin.site.register(Variant)
admin.site.register(FuturedImages)
admin.site.register(SizesOption)
admin.site.register(ColorsOption)
admin.site.register(Sliders)
admin.site.register(Comments)


