from django.db.models import query
from django.db.models.fields import UUIDField
from django.db.models.query import QuerySet
from rest_framework import serializers
from rest_framework.decorators import APIView
from rest_framework.response import Response

from src.users.models import User
from src.users.serializers import UserSerializer
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

class HomeView(APIView):
    
      def get(self, request):
          return Response({"message":"cao"})

class UserViewSet(GenericAPIView, RetrieveModelMixin):

      queryset = User.objects.all()
      serializer_class = UserSerializer
      lookup_field = 'id'

      def get(self, request, *args, **kwargs):
          return self.retrieve(request, *args, **kwargs)

      
      



       
    
  



      
      
        
        




   
        

      
    

