# coding=utf-8


from newsfeels.settings.base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ADD_A_PROPER_VALUE_HERE',
        'USER': 'ADD_A_PROPER_VALUE_HERE',
        'PASSWORD': 'ADD_A_PROPER_VALUE_HERE',
        'HOST': 'ADD_A_PROPER_VALUE_HERE',
        'PORT': 'ADD_A_PROPER_VALUE_HERE',
    }
}

# ----------------------------------------------------------------------------------------------------------------------
# Custom settings, common for PROD env
# ----------------------------------------------------------------------------------------------------------------------
