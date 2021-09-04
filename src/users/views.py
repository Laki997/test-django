from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from src.users.models import User
from src.users.serializers import UserSerializer
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.mixins import RetrieveModelMixin

class HomeView(APIView):
    
      def get(self, request):
        return Response({"message":"cao"})
      
class UserViewSet(GenericAPIView, RetrieveModelMixin):

      queryset = User.objects.all()
      serializer_class = UserSerializer
      lookup_field = 'id'
      
      def get(self, request, *args, **kwargs):
          return self.retrieve(request, *args, **kwargs)

class UserView(RetrieveAPIView):
    
      def get(self, request, *args, **kwargs):
          permission_classes = [permissions.IsAuthenticated]
          authentication_classes = JWTAuthentication
          serializer= UserSerializer(request.user)
          return Response(serializer.data)
 