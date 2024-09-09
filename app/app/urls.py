"""
URL configuration for app project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user_create import views
from authentication.views import AdminLoginView

router = DefaultRouter()
router.register(r"admins", views.AdminDataViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("admin/login/", AdminLoginView.as_view(), name="admin_login"),
    path("api/", include(router.urls)),
]
