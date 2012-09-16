from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.accounts.views',
    url(r'login/$', 'login', name='login'),
    url(r'logout/$', 'logout', name='logout'),
    url(r'profile/$', 'profile', name='profile'),
    url(r'xhr/reload/api/key/$',
        'generate_new_api_key', name='reload-api-key'),
)
