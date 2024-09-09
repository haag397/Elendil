"""serializer for admins and users
"""
from rest_framework import serializers

from .models import AdminData, UserData


class AdminDataSerializer(serializers.ModelSerializer):
    """serializer for UserData"""

    class Meta:
        model = AdminData
        fields = [
            "id",
            "email",
            "username",
            "password",
            "first_name",
            "last_name",
            "date_joined",  # Add this field if you want to display it
            "last_edit",
        ]
        read_only_fields = ["id", "date_joined", "last_edit"]
        extra_kwargs = {"password": {"write_only": True}}
        extra_kwargs = {"password": {"write_only": True}}


class UserDataSerializer(serializers.ModelSerializer):
    """serializer for UserData"""

    class Meta:
        model = UserData
        fields = ["id", "username", "password", "email", "first_name", "last_name"]
        read_only_fields = ["id", "date_joined", "last_edit"]
        extra_kwargs = {"password": {"write_only": True}}
