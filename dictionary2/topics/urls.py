# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^ajax/get-today/$', views.get_today, name='get_today'),
    url(r'^ajax/get-popular/$', views.get_popular, name='get_popular'),
    url(r'^ajax/get-junior_user/$', views.get_junior_user, name='get_junior_user'),
    url(r'^ajax/get-stray/$', views.get_stray, name='get_stray'),
    url(r'^ajax/get-category/$', views.by_category, name='by_category'),


    # url(r'^today/$', views.today, name='today'),
    # url(r'^populer/$', views.populer, name='populer'),
    # url(r'^badi/$', views.populer, name='badi'),
    # url(r'^caylak/$', views.caylak, name='caylak'),
    # url(r'^basiboslar/$', views.basiboslar, name='basiboslar'),
    # url(r'^entry/$', views.entry, name='entry'),

    # url(r'^favorite/$', views.favorite, name='favorite'),

]
