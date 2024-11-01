from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import RegisterView, GetTokenView


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('get-token/', GetTokenView.as_view()),
]