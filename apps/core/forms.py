# coding: utf-8
#
from django import forms
from apps.core.models import Image, Comment
from django.utils.translation import ugettext_lazy as _
#from django.forms.util import ErrorList
#from apps.core.helpers import get_object_or_None
#from django.utils.translation import ugettext_lazy as _


class AddImageForm(forms.ModelForm):
    required_css_class = 'required'
    next = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Image
        exclude = ['object_id', 'content_type', 'thumbnail', ]

class EditImageForm(AddImageForm):
    provide_initial_values = True
    next = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Image
        exclude = ['object_id', 'content_type', 'image']

class ActionCommentForm(forms.ModelForm):
    required_css_class = 'required'
    next = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Comment
        exclude = ['object_id', 'content_type', 'author', 'datetime' ]
        widgets = {
            'comment': forms.Textarea(),
        }

class RequestModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        if 'request' in kwargs:
            self.request = kwargs['request']
            del kwargs['request']
        super(RequestModelForm, self).__init__(*args, **kwargs)

class TestIFree(forms.Form):
    text = forms.CharField(required=True, label=_('Text'))
    sender = forms.CharField(required=True, label=_('From'))
    to = forms.CharField(required=True, label=_('To'))
