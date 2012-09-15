# Create your views here.
# coding: utf-8
from apps.core.helpers import render_to

@render_to('index.html')
def index(request):
    return {}
