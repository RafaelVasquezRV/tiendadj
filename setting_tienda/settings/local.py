from .base import *
from .db import *

#
import firebase_admin
from firebase_admin import credentials, auth

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = DB_POSTGRESQL

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

cred = credentials.Certificate("fbkey.json")
firebase_admin.initialize_app(cred)