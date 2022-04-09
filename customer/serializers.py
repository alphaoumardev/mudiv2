from rest_framework import serializers
from .models import CustomerProfile

# from orders.models import *
# from users.models import *
# from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True,)

    class Meta:
        model = CustomerProfile
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {'password':{'write_only':True}}

    def save(self, **kwargs):
        user = CustomerProfile(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': "The password must match"})
        user.set_password(password)
        user.save()
        return user

class CustomerPropertiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerProfile
        fields = "__all__"
        # fields = ['pk', 'email', 'username', ]

# class CustomerProfileSerializer(serializers.ModelSerializer):
#     avatar = serializers.SerializerMethodField(read_only=True)
#
#     class Meta:
#         model = CustomerProfile
#         fields = '__all__'
#
#     def get_avatar(self, obj):
#         try:
#             avatar = obj.avatar.url
#         except:
#             avatar = None
#         return avatar
#
#
# class CurrentUserSerializer(serializers.ModelSerializer):
#     profile = serializers.SerializerMethodField(read_only=True)
#
#     class Meta:
#         model = User
#         fields = ['id', 'profile', 'username', 'email', 'is_superuser', 'is_staff']
#
#     def get_profile(self, obj):
#         profile = obj.userprofile
#         serializer = CustomerProfileSerializer(profile, many=False)
#         return serializer.data
#
#
# class UserSerializer(serializers.ModelSerializer):
#     profile = serializers.SerializerMethodField(read_only=True)
#
#     class Meta:
#         model = User
#         fields = ['id', 'profile', 'username', 'is_superuser', 'is_staff']
#
#     def get_profile(self, obj):
#         profile = obj.userprofile
#         serializer = CustomerProfileSerializer(profile, many=False)
#         return serializer.data
#
#
# class CustomerSerializerWithToken(UserSerializer):
#     access = serializers.SerializerMethodField(read_only=True)
#     refresh = serializers.SerializerMethodField(read_only=True)
#
#     class Meta:
#         model = User
#         exclude = ['password']
#
#     def get_access(self, obj):
#         token = RefreshToken.for_user(obj)
#
#         token['username'] = obj.username
#         token['name'] = obj.userprofile.name
#         token['avatar'] = obj.userprofile.avatar.url
#         token['is_staff'] = obj.is_staff
#         token['id'] = obj.id
#         return str(token.access_token)
#
#     def get_refresh(self, obj):
#         token = RefreshToken.for_user(obj)
#         return str(token)
