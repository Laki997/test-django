from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from src.users.models import User
from src.users.serializers import UserSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from .permissions import UserPermissions


class HomeView(GenericAPIView):

    def get(self, request):
        return Response({"message": "cao"})


class UserViewSet(GenericViewSet, RetrieveModelMixin, CreateModelMixin):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    permission_classes = [UserPermissions, ]

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @action(detail=False, methods=['GET'], url_path='me', url_name='me',
            permission_classes=[IsAuthenticated],
            authentication_classes=[JWTAuthentication])
    def get_current_user(self, request):
        serializer = UserSerializer(self.request.user)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'], url_path=r'name/(?P<name>\w+)',
            url_name='name')
    def filter_by_first_or_last_name(self, request, name):
        users = User.objects.filter_name(name)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
