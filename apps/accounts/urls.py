from django.conf.urls import patterns, include, url
from apps.core.shortcuts import direct_to_template

urlpatterns = patterns('apps.accounts.views',
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^profile/$', 'profile', name='profile'),
    url(r'^register/$', 'register', name='register'),
    url(r'^invite/$', 'invite', name='invite'),
    url(r'^invite/register/success/$', direct_to_template,
        {'template': 'accounts/invite_register_success.html'},
        name='invite-register-success'),
    url(r'^invite/success/$', direct_to_template,
        {'template': 'accounts/invite_success.html'},
        name='invite-success'),
    url(r'^invite/register/(?P<sid>[\w\d]+)/$',
        'invite_register', name='invite-register'),
    url(r'password/(?P<sid>[\w\d]+)/restore/$', 'password_restore',
        name='password-restore'),
    url(r'password/restore/initiate/$', 'password_restore_initiate',
        name='password-restore-initiate'),
    url(r'profile/password/change/$', 'password_change',
        name='password-change'),
    url(r'password/changed/$', direct_to_template,
        {'template': 'accounts/password_changed.html'},
        name='password-changed'),
    url(r'^xhr/reload/api/key/$',
        'generate_new_api_key', name='reload-api-key'),
)
