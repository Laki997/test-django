from django.urls import path
from .views import HomeView,UserViewSet

urlpatterns = [
   path('', HomeView.as_view()),
   path('users/<id>', UserViewSet.as_view())
]
