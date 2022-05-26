from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import UserAccount
from accounts.serializers import UserCreateSerializer


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
