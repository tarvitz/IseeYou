# Create your views here.
# -*- coding: utf-8 -*-
from apps.core.helpers import render_to, ajax_response
from apps.core.decorators import login_required_json
from apps.accounts.forms import LoginForm

from django.contrib import auth

@render_to('accounts/login.html')
def login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.cleaned_data['user']
            auth.login(request, user)
            return {'redirect': 'core:index'}
    return {
        'form': form
    }

@render_to('index.html')
def logout(request):
    auth.logout(request)
    return {}

@render_to('accounts/profile.html')
def profile(request):
    return {}

@login_required_json
@ajax_response
def generate_new_api_key(request):
    if request.method == 'POST':
        request.user.api_key.key = request.user.api_key.generate_key()
        request.user.api_key.save()
        key = request.user.api_key.key
        return {'success': True, 'key': key}
    return {'success': False}
