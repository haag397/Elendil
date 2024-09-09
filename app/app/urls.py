"""
URL configuration for app project.
"""
from django.contrib import admin
from django.urls import path
from authentication.views import User
from core.views import AdminDataCreateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", User.as_view(), name="user-list-create"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("createadmin/", AdminDataCreateView.as_view(), name="admin-data-create"),
]
