from django.conf.urls import patterns, include, url
from apps.core.shortcuts import direct_to_template

urlpatterns = patterns('apps.news.views',
    url(r'^$', 'news', name='news'),
    url(r'^(?P<pk>\d+)/$', 'article', name='article'),
)
