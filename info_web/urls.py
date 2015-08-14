from django.conf.urls import patterns, include, url
from django.contrib import admin

import users.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'info_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include(users.urls, namespace='users')),
)