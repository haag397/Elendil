"""
settings for development
"""
from .base import *

ALLOWED_HOSTS = ["0.0.0.0"]

import os

def read_secret(secret_name):
    try:
        with open(f"/run/secrets/database_password") as f:
            return f.read().strip()
    except IOError:
        return None

print("==================================")
print(read_secret("database_password"))
print("********************************************")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'root',
       "PASSWORD": read_secret("database_password"),
        # 'PASSWORD': '2izqnc9vfy2aw2iqbjk903s75',
        'HOST': 'db',
        'PORT': '5432',
    }
}
