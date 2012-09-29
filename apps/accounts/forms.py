# -*- coding: utf-8 -*-
from django import forms
from django.forms.util import ErrorList
from django.utils.translation import ugettext_lazy as _

from django.contrib import auth
from django.contrib.auth.models import User

from apps.core.helpers import get_object_or_None


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


class AccountRegisterForm(forms.ModelForm):
    password2 = forms.CharField(
        required=True, label=_("Repeat password"),
        help_text=_("Repeat password"),
        widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data['username']
        user = get_object_or_None(User, username__iexact=username)
        if user:
            raise forms.ValidationError(
                _("Sorry but such username already taken, \
                  please choose another or login"))
        return username

    def clean(self):
        cd = self.cleaned_data
        password = cd.get('password') or None
        password2 = cd.get('password2') or None

        if all((password, password2)):
            if password != password2:
                msg = _("Passwords does not match, please correct them")
                self._errors['password'] = ErrorList([msg])
                if 'password' in cd:
                    del cd['password']
        return cd

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
