# coding: utf-8

from apps.core.helpers import get_object_or_None
from django.db import models
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User
from uuid import uuid1


class UserSIDManager(models.Manager):
    def create(self, user):
        sid = uuid1().hex
        
        if not user:
            return None

        instance = self.model(user=user, sid=sid)
        instance.save()
        return instance
