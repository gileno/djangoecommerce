# coding=utf-8

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^alterar-dados/$', views.update_user, name='update_user'),
    url(r'^registro/$', views.register, name='register'),
]
