from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django_countries import countries

from mart.serializers import *
from orders.serializers import CartItemSerializer


@api_view(["GET", "POST", "DELETE"])
def get_cart(request):
    if request.method == 'GET':
        items = CartItem.objects.all()
        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        pass


@api_view(["GET"])
@permission_classes([AllowAny])
def get_countries(request, *args, **kwargs):
    return Response(countries, status=HTTP_200_OK)


# Create your views here.
