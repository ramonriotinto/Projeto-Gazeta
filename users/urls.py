from django.urls import path
from .views import CreateAPIView, ListUsers, ListUpdateDeleteAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("users/", CreateAPIView.as_view()),
    path("listusers/", ListUsers.as_view()),
    path("users/<uuid:user_id>/", ListUpdateDeleteAPIView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
]
