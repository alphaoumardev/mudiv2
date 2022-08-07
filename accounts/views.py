from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import UserAccount, UserProfile
from accounts.serializers import UserCreateSerializer, UserProfileSerializer


@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def update_user_profile(request):
    user = request.user.id
    if request.method == 'PUT':
        account = UserAccount.objects.get(id=user)
        seriliazer = UserCreateSerializer(instance=account, data=request.data)
        if seriliazer.is_valid():
            seriliazer.save()
        return Response(seriliazer.data)


@permission_classes([IsAuthenticated])
@api_view(['POST', 'PUT', 'GET'])
def create_user_profile(request):
    if request.method == "POST":
        serializer = UserProfileSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == "GET":
        user = request.user
        profile = UserProfile.objects.filter(user=user)
        serializer = UserProfileSerializer(profile, many=True)
        return Response(serializer.data)
    if request.method == "PUT":
        user = request.user.id
        account = UserProfile.objects.get(id=user)
        seriliazer = UserProfileSerializer(instance=account, data=request.data)
        if seriliazer.is_valid():
            seriliazer.save()
        return Response(seriliazer.data)
