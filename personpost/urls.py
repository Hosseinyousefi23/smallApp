from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>[0-9]*)$', views.personPage, name='personpost_personPage'),
    url(r'^$', views.mainPage, name='personpost_mainPage'),
    url(r'^post/$', views.post, name='personpost_post'),
]
