# coding=utf-8
"""
This module contains environment-specific settings for this project to work LOCALLY.
e.g. DB credentials, API keys, custom paths, etc.

-----------------------------------------------------------------------------------------------------------------------
HOW TO MANAGE YOUR LOCAL SETTINGS:
1. Please make a copy of this file inside this same package
2. Rename it `local.py`
3. Modify all values inside `local.py` accordingly

If you need to add more custom settings or tweaks, do it in directly at the end of `local.py`.
-----------------------------------------------------------------------------------------------------------------------
"""

from newsfeels.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ADD_A_PROPER_VALUE_HERE',
        'USER': 'ADD_A_PROPER_VALUE_HERE',
        'PASSWORD': 'ADD_A_PROPER_VALUE_HERE',
        'HOST': 'ADD_A_PROPER_VALUE_HERE',
        'PORT': 'ADD_A_PROPER_VALUE_HERE',
    }
}

# ----------------------------------------------------------------------------------------------------------------------
# Custom settings, common for LOCAL env
# ----------------------------------------------------------------------------------------------------------------------
