# coding: utf-8
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.utils.translation import ugettext_lazy as _, ugettext as _tr
from apps.core.helpers import get_object_or_None
from django.dispatch import receiver
from apps.accounts.models import Invite, User
from django.core.exceptions import ObjectDoesNotExist


__all__ = ['invite_user', 'setup_signals']


@receiver(post_save, sender=Invite)
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

def setup_signals():
    post_save.connect(invite_user, sender=Invite)
