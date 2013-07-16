#coding: utf-8
from django import forms
from django.db import models
from django.db.models import Q,F
from django.contrib import admin
from apps.accounts.models import Invite
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from apps.accounts.models import User

class InviteAdmin(admin.ModelAdmin):
    list_display = ('sender', 'email', 'is_verified', 'created_on')
admin.site.register(Invite, InviteAdmin)


class UserCreationForm(forms.ModelForm):
    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }
    username = forms.RegexField(label=_("Username"), max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text=_("Required. 30 characters or fewer. Letters, digits and "
                      "@/./+/-/_ only."),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('username', )


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User


UserAdmin.form = UserAdminForm
UserAdmin.add_form = UserCreationForm

UserAdmin.fieldsets[1][1]['fields'] = ('first_name', 'last_name', 'email', )
admin.site.register(User, UserAdmin)
