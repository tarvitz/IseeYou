# coding: utf-8
from settings.dist import *
from settings.local import *
from settings.dist import INSTALLED_APPS

DEBUG=True
DEV_SERVER=True
USER_FILES_LIMIT=1.2*1024*1024
SEND_MESSAGES=False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '_test.sqlite',
    }, 
}
INSTALLED_APPS = list(INSTALLED_APPS)
removable = ['south', ]
for app in removable:
    if app in INSTALLED_APPS:
        INSTALLED_APPS.remove(app)

TEST_DATABASE_NAME = DATABASES['default']['NAME'] if \
    DATABASES['default']['NAME'].startswith('test_') else \
    'test_' + DATABASES['default']['NAME']

#
def _to_uni(value):
    try:
        return str(value)
    except:
        try:
            return str(value.message.encode('utf-8'))
        except:
            return '<unprintable %s object>' % type(value).__name__
import traceback
traceback._some_str = _to_uni
