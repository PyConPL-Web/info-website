from django.conf.urls import patterns, include, url
from newsy import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'info_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^[/]$', views.index, name='index'),
    url(r'^datail/(?P<permalink>.*)[/]$', views.detail, name='detail'),
)
