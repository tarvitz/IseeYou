# -*- coding: UTF-8 -*-
from django import forms
from hvad.forms import TranslatableModelForm
from django.db.utils import IntegrityError
from django.utils.translation import ugettext_lazy as _
from apps.news.models import News


class NewsAdminForm(TranslatableModelForm):
    class Meta:
        widgets = {
            'content': forms.Textarea
        }
        fields = ('title', 'content', )
