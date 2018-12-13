# coding=utf-8


import django_heroku

from newsfeels.settings.base import *

DEBUG = False
ALLOWED_HOSTS = ['https://newsfeels-jcpmmx.herokuapp.com',]

# ----------------------------------------------------------------------------------------------------------------------
# Custom settings, common for PROD env
# ----------------------------------------------------------------------------------------------------------------------

django_heroku.settings(locals())
