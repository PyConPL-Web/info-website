from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'info_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^news[/]', include('newsy.urls', namespace='newsy')),
    url(r'^admin[/]', include(admin.site.urls)),
)
