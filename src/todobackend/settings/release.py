from .base import *
import os


# Disable debug
if os.environ.get('DEBUG'):
    DEBUG = True
else:
    DEBUG = False

# Must be explicitly specified when Debug is disabled
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS', '*')]

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME','postgres'),
        'USER': os.environ.get('DATABASE_USER','postgres'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD','postgres'),
        'HOST': os.environ.get('DATABASE_HOST','db'),
        'PORT': os.environ.get('DATABASE_PORT','5432'),
    }
}

STATIC_ROOT = os.environ.get('STATIC_ROOT', '/var/www/todobackend/static')
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', '/var/www/todobackend/media')