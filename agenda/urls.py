from django.conf.urls import patterns, include, url
from django.contrib import admin
from agenda import models

urlpatterns = patterns('', url(r'^$', 'agenda.views.index', name='index'),)