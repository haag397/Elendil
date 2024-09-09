"""define all models here
"""
from django.db import models
from uuid import uuid4


class AdminData(models.Model):
    """
    Admin model
    """

    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=40, unique=True, null=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True, blank=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["username", "password", "email", "lastname"]

    def __str__(self):
        return self.username


class UserData(models.Model):
    """
    User model
    """

    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
    password = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=40, unique=True, null=True)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)
    created_by_id = models.ForeignKey(AdminData, on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["password", "username", "email", "lastname"]

    def __str__(self):
        return self.username
