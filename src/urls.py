from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from src.users.urls import users_router
from src.users.views  import HomeView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()

router.registry.extend(users_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('api/', include(router.urls)),
    path('api/login', TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view())
]
