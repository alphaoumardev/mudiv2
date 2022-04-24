from django.urls import path
from .views import *

urlpatterns = [
    # The orders
    path('order/', get_cart, name='orders'),
    path('countries/', get_countries, name='countries'),
    path('cart/', CartItemViews.as_view(), name='hw'),
    path('cart/<str:pk>', CartItemViews.as_view(), name='cart_items'),

    path('orders/', get_orders, name='get_orders'),
    path('orders/add/', add_order_items, name='add_order_items'),
    path('orders/myorder/', get_my_orders, name='get_my_orders'),
    path('orders/<str:pk>/', get_order_by_id, name='get_order_by_id'),
    path('orders/<str:pk>/deliver/', update_order_to_delivered, name='update_order_to_delivered'),
    path('orders/<str:pk>/pay/', update_order_to_paid, name='update_order_to_paid'),
]
