"""_summary_
"""
from rest_framework import serializers

from .models import AdminData, UserData


class AdminDataSerializer(serializers.ModelSerializer):
    """serializer for UserData"""

    class Meta:
        model = AdminData
        fields = [
            "email",
            "firstname",
            "lastname",
            "is_active",
            "username",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }


class UserDataSerializer(serializers.ModelSerializer):
    """serializer for UserData"""

    class Meta:
        model = UserData
        fields = [
            "email",
            "firstname",
            "lastname",
            "is_active",
            "username",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }
