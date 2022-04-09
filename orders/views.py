from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, views, viewsets
from rest_framework.pagination import PageNumberPagination
from mart.serializers import *


@api_view(["GET", "POST", "DELETE"])
def get_cart(request):
    if request.method == 'GET':
        items = CartItem.objects.all()
        serializer = CartItemModel(items, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        pass

# Create your views here.
