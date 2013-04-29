# -*- coding: utf-8 -*-
from django import forms
from django.forms.util import ErrorList
from django.utils.translation import ugettext_lazy as _

from django.contrib import auth
from django.contrib.auth.models import User
from django.conf import settings

from apps.core.helpers import get_object_or_None
from apps.core.forms import (
    RequestModelForm, BruteForceCheck
)
from apps.accounts.models import Invite
from apps.core.models import UserSID

from uuid import uuid1


class LoginForm(forms.Form):
    username = forms.CharField(label=_("Username"))
    password = forms.CharField(
        label=_("Password"), widget=forms.PasswordInput())

    def clean(self):
        cd = self.cleaned_data
        username = cd.get('username')
        password = cd.get('password')
        user = auth.authenticate(username=username, password=password)

        if not user:
            # fail to authenticate, probabbly incorrect auth data
            msg = _("Sorry your username or/and password are invalid")
            self._errors['password'] = ErrorList([msg])
            if 'password' in cd:
                del cd['password']

        cd['user'] = user
        return cd


class AccountRegisterForm(forms.ModelForm):
    username = forms.RegexField(
        label=_("Username"),
        regex=re.compile(r'^[A-z][\w\d\._-]+\w+$'),
        max_length=32,
        min_length=3,
        error_message=_('Try to pass only latin symbols, numbers and underscores with your nickname'),
        help_text=_('Only latin symbols and numbers and underscore are allowed'),

    )
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
        widgets = {
            'password': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }


class InviteRegisterForm(AccountRegisterForm):
    username = forms.RegexField(
        label=_("Username"),
        regex=re.compile(r'^[A-z][\w\d\._-]+\w+$'),
        max_length=32,
        min_length=3,
        error_message=_('Try to pass only latin symbols, numbers and underscores with your nickname'),
        help_text=_('Only latin symbols and numbers and underscore are allowed'),

    )
    password = forms.CharField(
        label=_("Password"), required=True,
        widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', )


class SendInviteForm(RequestModelForm):
    def clean(self):
        cd = self.cleaned_data
        user = self.request.user
        if user.invites >= settings.MAX_INVITES_COUNT:
            msg = _("Your are out of invite limit, sorry for that :)")
            self._errors['email'] = ErrorList([msg])
            if 'email' in cd:
                del cd['email']
        return cd

    def save(self, commit=True):
        super(SendInviteForm, self).save(commit=commit)
        self.instance.sid = uuid1().get_hex()
        self.instance.sender = self.request.user

    class Meta:
        model = Invite
        fields = ('email', )


class PasswordRestoreInitiateForm(forms.Form):
    email = forms.CharField(
        label=_("Email"), help_text=_("Your email")
    )

    def clean_email(self):
        email = self.cleaned_data['email'] or None
        users = User.objects.filter(email__iexact=email)
        if not users:
            raise forms.ValidationError(
                _("Users with given email does not exists")
            )
        self.cleaned_data['users'] = users
        return email


class PasswordRestoreForm(RequestModelForm, BruteForceCheck):
    password = forms.CharField(
        label=_("Password"), widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label=_("Password repeat"), widget=forms.PasswordInput()
    )

    def clean(self):
        cd = self.cleaned_data
        password = cd['password']
        password2 = cd['password2']
        if all((password, password2) or (None, )):
            if password != password2:
                msg = _("Passwords don't match")
        return cd

    def save(self, commit=True):
        user = self.instance.user
        user.set_password(self.cleaned_data['password'])
        user.save()
        if commit:
            self.instance.expired = True
            self.instance.save()
            instance = self.instance
        else:
            instance.expired = True
            instance = super(Password, self).save(commit=commit)

        return instance

    class Meta:
        model = UserSID
        exclude = ('expired_date', 'expired', 'sid', 'user')


class PasswordChangeForm(forms.ModelForm):
    old_password = forms.CharField(
        label=_("Old password"), widget=forms.PasswordInput()
    )
    new_password = forms.CharField(
        label=_("New password"), widget=forms.PasswordInput()
    )
    new_password_repeat = forms.CharField(
        label=_("New password repeat"), widget=forms.PasswordInput()
    )

    def clean(self):
        cd = self.cleaned_data
        old_password = cd['old_password']
        new_pwd = cd['new_password']
        new_pwd_repeat = cd['new_password_repeat']
        user = auth.authenticate(
            username=self.instance.username, password=old_password
        )
        if not user:
            msg = _("Old password does not match")
            self._errors['password'] = ErrorMsg([msg])
            if 'password' in cd:
                del cd['password']
        if all((new_pwd, new_pwd_repeat) or (None, )):
            if new_pwd != new_pwd_repeat:
                msg = _("Passwords don't match")
                self._errors['new_password'] = ErrorList([msg])
                if 'new_password' in cd:
                    del cd['new_password']
        return cd

    def save(self, commit=True):
        self.instance.set_password(self.cleaned_data['new_password'])
        self.instance.save()
        super(PasswordChangeForm, self).save(commit)


    class Meta:
        model = User
        fields = []
