from django.conf.urls.defaults import patterns, include, url
from apps.core.shortcuts import direct_to_template


urlpatterns = patterns('apps.core.views',
    url(r'^$', 'index', name='index'),
    url(r'^test/$', 'test', name='test'),
    url(r'^extensions/chrome/$', 'chrome_extension', name='chrome-extension'),
    #static
    url(r'^function/blocked/$', direct_to_template,
        {'template': 'static/function_blocked.html'},
        name='blockage'),
    url(r'^faq/$', direct_to_template,
        {'template': 'static/faq.html'},
        name='faq'),
    url(r'^configuration/$', direct_to_template,
        {'template': 'static/configuration.html'},
        name='configuration'),
    url(r'^about/$', direct_to_template,
        {'template': 'static/about.html'},
        name='about'),
    url(r'^contacts/$', direct_to_template,
        {'template': 'static/contacts.html'},
        name='contacts'),
    url(r'^features/$', direct_to_template,
        {'template': 'static/features.html'},
        name='features'),
    url(r'^does/not/exists/$', direct_to_template,
        {'template': 'static/does_not_exists.html'},
        name='does-not-exists'),
    url(r'^file/not/found/$', direct_to_template,
        {'template': 'static/file_not_found.html'},
        name='file-not-found'),
)
