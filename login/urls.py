from django.contrib.auth import views as auth_views
from django.conf.urls import patterns, include, url

from login import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
)