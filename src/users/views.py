from rest_framework.decorators import APIView
from rest_framework.response import Response

from src.users.models import User
from src.users.serializers import UserSerializer
from rest_framework.generics import RetrieveAPIView

class HomeView(APIView):
    
      def get(self, request):
          return Response({"message":"cao"})

class UserViewSet(RetrieveAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer
        lookup_field='pk'
        # lookup_url_kwarg='pk'
        
        # def get(self, request, *args, **kwargs):
        #     return self.retrieve(request, *args, **kwargs)




   
        

      
    

