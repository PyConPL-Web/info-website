from django.conf.urls import patterns, include, url
from users import views

urlpatterns = patterns('',
                       url(r'^index[/]$', views.index, name='index'),
                       url(r'^$', views.login, name='login'),
                       url(r'^signup[/]$', views.signup, name='signup'),
                       url(r'^validate_user[/]$', views.validate_user, name='validate_user'),
                       url(r'^confirm_user/(?P<confirm_string>[0-9a-zA-Z]{16})$', views.confirm_user, name='confirm_user'),
)