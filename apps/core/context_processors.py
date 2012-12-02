# coding: utf-8
from django.contrib.sites.models import Site
from datetime import datetime, timedelta, time
from django.conf import settings
from django.utils import translation


def language(request):
    language = request.session.get('language', 'en')
    translation.activate(language)
    return {
        'LANGUAGE_CODE': translation.get_language(),
    }

def global_referer(request):
    return {
        'current_referer': "http://%s%s" % (
            request.META.get("HTTP_HOST", "localhost"),
            request.META.get('PATH_INFO', '/')),
        'global_referer': request.META.get('HTTP_REFERER', '/')
    }


def global_settings(request):
    return {
        'global_settings': settings,
        'gs': settings,
        'get_full_path': request.get_full_path(),
        'current_date': datetime.today(),
        'global_site': Site.objects.get(),
    }


def session(request):
    return {
        'session': request.session,
    }


def template(request):
    return {
        'base': settings.DEFAULT_TEMPLATE
    }
