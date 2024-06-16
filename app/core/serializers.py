"""_summary_
"""

from rest_framework import serializers

# from .models import UserData
from .models import UserData


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
            "is_superuser",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }
