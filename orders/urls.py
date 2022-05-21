from django.urls import path
from .views import *

urlpatterns = [
    # The orders
    path('cart/', create_cart, name='cart'),

    path('cart/<str:pk>', CartItemView.as_view(), name='cart_items'),
    path('wishlist/', create_wishlist, name='wishlist'),
    path('wishlist/<str:pk>', operate_wishlist, name='wishlist'),
    path('address/', create_address,  name='address'),
    path('orders/', create_order, name='orders'),
    path('orderitem/<str:pk>', create_orderItem, name='orderItem'),


    # path('order/<str:pk>', OrderView.as_view(), name='orders'),
    # path('countries/', get_countries, name='countries'),
    # path('orders/', get_orders, name='get_orders'),
    # path('orders/add/', add_order_items, name='add_order_items'),
    path('orders/myorder/', get_my_orders, name='get_my_orders'),
    path('orders/<str:pk>/', get_order_by_id, name='get_order_by_id'),
    path('orders/<str:pk>/deliver/', update_order_to_delivered, name='update_order_to_delivered'),
    path('orders/<str:pk>/pay/', update_order_to_paid, name='update_order_to_paid'),
]
