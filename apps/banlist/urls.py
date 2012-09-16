from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.banlist.views',
    url(r'^$', 'index', name='index'),
    url(r'^add/$', 'add', name='add'),
)
