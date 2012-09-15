# Create your views here.
# -*- coding: utf-8 -*-
from apps.core.helpers import render_to
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
