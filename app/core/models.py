"""_summary_
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserData(AbstractBaseUser):
    """
    user info
    """

    email = models.EmailField(max_length=50, unique=True)
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)
    username = models.CharField(max_length=20, unique=True)
    is_superuser = models.BooleanField(default=False)

    # objects = UserDataManager()
    REQUIRED_FIELDS = ["email", "firstname", "lastname", "is_active", "username"]

    def __str__(self):
        return str(self.email)
