from django.db.models.base import Model
from rest_framework.decorators import APIView, action, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from src.users.models import User
from src.users.serializers import UserSerializer
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet

class HomeView(GenericAPIView):
     
      def get(self, request):
        return Response({"message":"cao"})
      
class UserViewSet(GenericViewSet, RetrieveModelMixin):

      queryset = User.objects.all()
      serializer_class = UserSerializer
      lookup_field = 'id'
      
      def get(self, request, *args, **kwargs):
          return self.retrieve(request, *args, **kwargs)

      @action(detail=False, methods=['GET'], url_path='me', url_name='me', permission_classes=[IsAuthenticated], authentication_classes=[JWTAuthentication])
      def get_current_user(self, request):
          serializer = UserSerializer(self.request.user)
          return Response(serializer.data)
