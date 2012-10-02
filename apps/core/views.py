# Create your views here.
# coding: utf-8
import os
from apps.core.helpers import render_to, ajax_response
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect


@render_to('index.html')
def index(request):
    if request.user.is_authenticated():
        return {'redirect': 'banlist:index'}
    return {}


@ajax_response
def test(request):
    return {
        'success': True
    }


def chrome_extension(request):
    filename = os.path.join(settings.PROJECT_ROOT, 'media/chrome/bf3ban.crx')
    if not os.path.exists(filename):
        return redirect('core:file-not-found')
    ext = open(filename, 'r')
    response = HttpResponse()
    response['Content-Type'] = 'application/x-chrome-extension'
    response.write(ext.read())
    return response
