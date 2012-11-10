# -*- coding: utf-8 -*-
from apps.accounts.models import Invite
from apps.core.helpers import get_object_or_None
from django.shortcuts import redirect
from django.http import Http404

from django.conf import settings

from datetime import datetime


def check_invite(sid):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            now = datetime.now()
            secure_id = kwargs[sid]
            invite = get_object_or_None(
                Invite, sid__iexact=secure_id, expire_date__gte=now
            )
            if not invite:
                return redirect('core:ufo')
            return func(request, *args, **kwargs)
        return wrapper
    return decorator


def prevent_bruteforce(func):
    def wrapper(request, *args, **kwargs):
        if request.session.get(
            'brute_force_iter', 0
        ) > settings.BRUTEFORCE_ITER:
            # should login bastards
            raise Http404(":D fuck you!")
        return func(request, *args, **kwargs)
    return wrapper
