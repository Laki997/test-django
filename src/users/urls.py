from django import urls
from django.db.backends.base import base
from .views import UserViewSet
from rest_framework import routers

users_router = routers.SimpleRouter()
users_router.register(r'users',UserViewSet,basename='users')
