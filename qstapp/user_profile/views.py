from django.shortcuts import render

# permissions
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )
    @action(detail=False) # retrieve current_user
    def me(self, request, *args, **kwargs):
        serializer_context = {
            'request': request,
        }
        user = get_object_or_404(User, id=request.user.id)
        return Response(UserSerializer(request.user, context=serializer_context).data,
                        status=status.HTTP_200_OK)