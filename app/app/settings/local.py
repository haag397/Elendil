"""
settings for development
"""
from .base import *
# import os
# DOCKER_SECRET_FILE = "/run/secrets/database_password"
# * Read the password from the Docker secret file
# with open(DOCKER_SECRET_FILE, "r") as file:
#     DOCKER_SECRET_PASSWORD = file.read().strip()
# try:
#     with open('/run/secrets/database_password') as f:
#         database_password = f.read().strip()
# except FileNotFoundError:
#         database_password = os.getenv('DATABASE_PASSWORD', 'qju9sj3yy1rdr21b0vudbjhfh')  # fallback
#         print("=====================================")
#         print("dddddddddddd",database_password)
ALLOWED_HOSTS = ["0.0.0.0"]


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "database",
#         "USER": "root",
#         "PASSWORD": database_password,
#         # "PASSWORD": "mypassword",
#         "HOST": "database",
#         # "HOST": "172.20.0.2",
#         "PORT": 5432,
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'root',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}
