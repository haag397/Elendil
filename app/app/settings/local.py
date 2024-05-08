"""
settings for development
"""
from .base import *

DOCKER_SECRET_FILE = "/run/secrets/database_password"
# * Read the password from the Docker secret file
with open(DOCKER_SECRET_FILE, "r") as file:
    DOCKER_SECRET_PASSWORD = file.read().strip()

ALLOWED_HOSTS = ["0.0.0.0"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "database",
        "USER": "myuser",
        "PASSWORD": DOCKER_SECRET_PASSWORD,
        # "HOST": "database",
        "HOST": "172.20.0.2",
        "PORT": 5432,
    }
}
