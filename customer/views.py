# Create your views here.
import datetime
import uuid
import random
import os.path

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
# email verification imports
from django.contrib.auth.tokens import default_token_generator
from django.core.files.storage import default_storage
# from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.db.models import Q, Count
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from email_validator import validate_email, EmailNotValidError
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated

from rest_framework.authtoken.models import Token

from .models import *
from .serializers import *
# from .signals import *

@api_view(['POST'])
@permission_classes([AllowAny])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            customer = serializer.save()
            data['response'] = "You have successfylly registered"
            data['email'] = customer.email
            data['username'] = customer.username
            token = Token.objects.get(user=customer).key
            data['token']=token
        else:
            data = serializer.errors
        return Response(data)

@action(detail=False, methods=['post'])
def logout(self, request):
    try:
        request.user.auth_token.delete()
    except (AttributeError, ObjectDoesNotExist):
        pass

    django_logout(request)
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_properties(request):
    try:
        customer = request.user
    except CustomerProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerPropertiesSerializer(customer)
        return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_customer_account(request):
    try:
        customer = request.user
    except CustomerProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CustomerPropertiesSerializer(customer, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = 'Your account is updated'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def email_validator(email):
#     """This is to validate and return the entered email if valide otherwise raise an exception """
#     try:
#         validated_email_data = validate_email(email)
#         email_add = validated_email_data['email']
#         return email_add
#     except EmailNotValidError as e:
#         return str(e)
#
#
# class RegisterApi(APIView):
#     permission_classes = [permissions.AllowAny]
#     authentication_classes = []
#
#     def post(self, request):
#         data = request.data
#         username = data.get('username')
#         email = data.get('email')
#         password = data.get('password')
#         # email_valid_check_result = email_validator(email)
#         messages = {'errors': []}
#         # if username or email or password == None:
#         #     messages['errors'].append("The username or the email cannot be empty")
#         # if not email_valid_check_result == email:
#         #     messages['errors'].append(email_valid_check_result)
#         if User.objects.filter(email=email).exists():
#             messages['errors'].append("This user already exists")
#         if User.objects.filter(username__iexact=username).exists():
#             messages['errors'].append("This username already exists")
#         if len(messages['errors']) > 0:
#             return Response({"detail": messages['errors']}, status=status.HTTP_400_BAD_REQUEST)
#         try:
#             new_user = User.objects.create(
#                 username=username,
#                 email=email,
#                 password=password
#             )
#             serializer = CustomerSerializerWithToken(new_user, many=False)
#         except Exception as e:
#             print(e)
#             return Response({"detail": f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.data)
#
# class LoginWithToken(APIView):
#
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#
#         token['username'] = user.username
#         token['name'] = user.userprofile.name
#         token['avatar'] = user.userprofile.avatar.url
#         token['is_staff'] = user.is_staff
#         token['id'] = user.id
#         return token
#     def validate(self, attrs):
#         data = super().validate(attrs)
#
#         serializer = CustomerSerializerWithToken(self.user).data
#         for k, v in serializer.items():
#             data[k]=v
#         return data
#
# class MyTokenPaiView(TokenObtainPairView):
#     serializer_class = LoginWithToken