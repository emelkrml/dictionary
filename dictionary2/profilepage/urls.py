from __future__ import absolute_import, unicode_literals
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^profil/$', views.profile, name='profile'),
    url(r'^ayarlar/$', views.ayarlar, name='ayarlar'),
    url(r'^mesajlar/$', views.messages, name='messages'),
    url(r'^olaylar/$', views.events, name='events'),

]
