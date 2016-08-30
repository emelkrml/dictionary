# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^s/$', views.entry_view, name='entry-view'),
    url(r'^today/$', views.today, name='today'),
    url(r'^populer/$', views.populer, name='populer'),
    url(r'^badi/$', views.populer, name='badi'),
    url(r'^caylak/$', views.populer, name='caylak'),
    url(r'^category/(?P<id>[0-9])/$', views.by_category, name='by-category'),
    url(r'^basiboslar/$', views.basiboslar, name='basiboslar'),
]
