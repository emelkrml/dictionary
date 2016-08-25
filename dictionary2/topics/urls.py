from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?P<slug>[^/]+)/$', views.topicView, name='topics'),
]
