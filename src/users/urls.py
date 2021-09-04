from django.urls import path
from .views import HomeView,UserViewSet, UserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
   path('', HomeView.as_view()),
   path('users/me', UserView.as_view()),
   path('users/<id>', UserViewSet.as_view()),
   path('login', TokenObtainPairView.as_view()),
   path('token/refresh', TokenRefreshView.as_view()),
]
