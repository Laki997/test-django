from django.db import models
from django.db.models.base import Model
from rest_framework import serializers
from src.users.models import User

class UserSerializer(serializers.ModelSerializer):
      class Meta:
         model = User
         fields = ('id','first_name','last_name','password','email')
         extra_kwargs = {'password': {'write_only' : True}}
