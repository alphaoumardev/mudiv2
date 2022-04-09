from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .models import *


# Register your models here.
# class CustomerAdmin(UserAdmin):
#     list_display = ('pk', 'email','username','date_joined', 'last_login', 'is_admin','is_staff')
#     search_fields = ('pk', 'email','username',)
#     readonly_fields=('pk', 'date_joined', 'last_login')
#
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()

admin.site.register(CustomerProfile,)
