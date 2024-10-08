"""
settings for development
"""
import os
from .base import *

ALLOWED_HOSTS = ["localhost"]


def read_secret(secret_name):
    """_summary_"""
    try:
        with open(f"/run/secrets/{secret_name}", "r") as file:
            return file.read().strip()
    except IOError:
        return None


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DATABASE_NAME"),
        "USER": os.environ.get("DATABASE_USER"),
        "PASSWORD": read_secret("database_password"),
        "HOST": os.environ.get("DATABASE_HOST"),
        "PORT": "5432",
    }
}
