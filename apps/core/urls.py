from django.conf.urls.defaults import patterns, include, url
from apps.core.shortcuts import direct_to_template


urlpatterns = patterns('apps.core.views',
    url('^$', 'index', name='index'),
    url('^test/$', 'test', name='test'),
    #static
    url(r'function/blocked/$', direct_to_template,
        {'template': 'static/function_blocked.html'},
        name='blockage'),
    url(r'faq/$', direct_to_template,
        {'template': 'static/faq.html'},
        name='faq'),
    url(r'does/not/exists/$', direct_to_template,
        {'template': 'static/does_not_exists.html'},
        name='does-not-exists'),
)

