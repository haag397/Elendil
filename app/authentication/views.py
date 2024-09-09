"""API for authentication
"""
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import AdminData
from core.serializers import AdminDataSerializer


class AdminLoginView(APIView):
    """handle login with JWT"""

    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        # * check username and password
        admin = authenticate(request, username=username, password=password)

        if admin is not None:
            # * Generate JWT tokens
            refresh = RefreshToken.for_user(admin)
            return Response(
                {
                    "refresh_token": str(refresh),
                    "access_token": str(refresh.access_token),
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"detail": "Invalid username or password"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
