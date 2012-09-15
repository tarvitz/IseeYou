from django.conf.urls.defaults import patterns, include, url
from apps.core.shortcuts import direct_to_template


urlpatterns = patterns('apps.core.views',
    url('^$', 'index', name='index'),
)

