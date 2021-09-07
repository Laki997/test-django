from django.contrib.auth.decorators import user_passes_test
from django.core.checks.messages import Error
from django.db.models.base import Model, ModelBase
from rest_framework.decorators import APIView, action, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from src.users.models import User
from src.users.serializers import UserSerializer
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from django.contrib.admin.views.decorators import staff_member_required
from .permissions import UserPermissions

class HomeView(GenericAPIView):
     
      def get(self, request):
        return Response({"message":"cao"})
      
class UserViewSet(GenericViewSet, RetrieveModelMixin, CreateModelMixin):

      queryset = User.objects.all()
      serializer_class = UserSerializer
      lookup_field = 'id'
      permission_classes = [UserPermissions,]
      
      def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

      @action(detail=False, methods=['GET'], url_path='me', url_name='me', permission_classes=[IsAuthenticated], authentication_classes=[JWTAuthentication])
      def get_current_user(self, request):
          serializer = UserSerializer(self.request.user)
          return Response(serializer.data)
