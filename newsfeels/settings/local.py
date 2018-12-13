# coding=utf-8


from newsfeels.settings.base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'newsfeels',
    }
}

# ----------------------------------------------------------------------------------------------------------------------
# Custom settings, common for LOCAL env
# ----------------------------------------------------------------------------------------------------------------------
