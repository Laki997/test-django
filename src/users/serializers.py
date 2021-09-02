from django.db import models
from django.db.models.base import Model
from rest_framework import serializers
from src.users.models import User

class UserSerializer(serializers.ModelSerializer):
      class Meta:
         model = User
         fields = ('id','username','first_name','last_name','password','email')
         extra_kwargs = {'password': {'write_only' : True}}
        #  read_only_fields = ('username')

        #  def create(self, validated_data):
        #      user = User.objects.create_user(**validated_data)
        #      return user


