# Create your views here.
# coding: utf-8
from apps.core.helpers import render_to, ajax_response


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
