from django.urls import path
from . import views

urlpatterns = [
    # The orders
    path('orders/', views.get_cart, name='orders'),

]