# coding=utf-8


from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('load/', views.load, name='load_articles'),
]
