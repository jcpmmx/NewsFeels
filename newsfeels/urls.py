# coding=utf-8


from django.contrib import admin
from django.urls import include, path

from articles import urls as articles_urls

urlpatterns = [
    path('articles/', include(articles_urls)),
    path('admin/', admin.site.urls),
]
