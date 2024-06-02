"""_summary_
"""
from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """_summary_

    Args:
        AbstractUser (_type_): _description_
    """

    # Custom fields for the user model
