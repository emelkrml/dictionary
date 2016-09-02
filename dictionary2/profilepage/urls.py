from __future__ import absolute_import, unicode_literals
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^p/$', views.profile_page, name='profile-page'),
    url(r'^ayarlar/$', views.ayarlar, name='ayarlar'),
    url(r'^mesajlar/$', views.mesajlar, name='mesajlar'),
]
