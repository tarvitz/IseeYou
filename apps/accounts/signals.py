# coding: utf-8
#
#try:
#    from django.contrib.auth import get_user_model
#    User = get_user_model()
#except ImportError:
#    from django.contrib.auth.models import User
from django.conf import settings
from apps.accounts.models import User
from django.db.models.signals import post_save, pre_save
from django.utils.translation import ugettext_lazy as _, ugettext as _tr
from apps.core.helpers import get_object_or_None
from django.dispatch import receiver
from apps.accounts.models import Invite
from django.core.exceptions import ObjectDoesNotExist

#from tastypie.models import create_api_key


__all__ = ['invite_user', 'create_api_key']


@receiver(post_save, sender=User)
def invite_user(instance, **kwargs):
    instance.sender.invites += 1
    instance.sender.save()
    return instance


@receiver(post_save, sender=User)
def create_api_key(instance, **kwargs):
    try:
        instance.api_key
    except ObjectDoesNotExist:
        from tastypie.models import ApiKey
        new_key = ApiKey.objects.create(user=instance)
    return instance

#def setup_signals():
#    post_save.connect(create_api_key, sender=User)
#    post_save.connect(invite_user, sender=Invite)
