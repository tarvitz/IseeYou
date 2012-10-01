# coding: utf-8
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.utils.translation import ugettext_lazy as _, ugettext as _tr
from apps.core.helpers import get_object_or_None

from tastypie.models import create_api_key


def setup_signals():
    post_save.connect(create_api_key, sender=User)
