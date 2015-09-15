from django.contrib.auth import views as auth_views
from django.conf.urls import patterns, include, url

from signup import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^confirm/(?P<confirm_string>[0-9a-zA-Z]{16})$',
                           views.confirm, name='confirm'),
)

