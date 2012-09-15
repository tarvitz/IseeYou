# -*- coding: utf-8 -*-
from django import forms
from django.forms.util import ErrorList
from django.utils.translation import ugettext_lazy as _

from django.contrib import auth

class LoginForm(forms.Form):
    username = forms.CharField(label=_("Username"))
    password1 = forms.CharField(
        label=_("Password"), widget=forms.PasswordInput())
    password2 = forms.CharField(
        _("Password repeat"), widget=forms.PasswordInput())

    def clean(self):
        cd = self.cleaned_data
        username = cd.get('username')
        password1 = cd.get('password1')
        password2 = cd.get('password2')
        if password1 != password2:
            msg = _("Sorry passwords you entered does not match each other")
            self._errors['password1'] = ErrorList([msg])
            if 'password1' in cd:
                del cd['password1']
        user = auth.authenticate(username=username, password=password1)
        if not user:
            # fail to authenticate, probabbly incorrect auth data
            msg = _("Sorry your username or/and password are invalid")
            self._errors['password1'] = ErrorList([msg])
            if 'password1' in cd:
                del cd['password1']
        
        cd['user'] = user
        return cd
