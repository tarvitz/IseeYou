#coding: utf-8
from django import forms
from django.db import models
from django.db.models import Q, F
from django.contrib import admin
from apps.news.models import News
from django.utils.translation import ugettext_lazy as _
from hvad.admin import TranslatableAdmin
from apps.news.adminforms import NewsAdminForm


class MediaAdmin(object):
    class Media:
        js = (
            '/media/js/tiny_mce/tiny_mce_src.js',
            '/media/js/textareas.js',
        )


class NewsAdmin(TranslatableAdmin, MediaAdmin):
    form = NewsAdminForm
    list_display = ('get_title', 'get_content', 'created_on', 'updated_on', )
    search_fields = ('title', 'content', 'created_on', 'updated_on')

    def get_title(self, obj):
        return obj.lazy_translation_getter('title', 'Title: %s' % obj.pk)
    get_title.short_description = _("Title")

    def get_content(self, obj):
        content = obj.lazy_translation_getter('content', 'Title: %s' % obj.pk)
        return content if len(content) < 50 else content[:50] + "..."
    get_content.short_description = _("Content")
admin.site.register(News, NewsAdmin)
