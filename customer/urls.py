from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

# app_name="users"
urlpatterns = [
    # The orders
    path('register/', views.registration_view, name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', views.logout, name='login'),
    path('update/', views.update_customer_account, name='update'),
    path('properties/', views.get_properties, name='properties'),
]
