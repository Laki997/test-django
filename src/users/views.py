from django.http import response
from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response

class HomeView(APIView):
    
      def get(self, request):
          return Response({"message":"cao"})

