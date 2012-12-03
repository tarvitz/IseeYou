from django.db import models
from django.utils.translation import ugettext_lazy as _

from datetime import datetime, timedelta

from hvad.models import TranslatableModel, TranslatedFields


# Create your models here.
class News(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("Title"), max_length=256),
            null=True,
        content = models.CharField(
            _("Content"), blank=True, null=True, max_length=8192)
    )
    updated_on = models.DateTimeField(
        _("updated on"), default=datetime.now,
        auto_now_add=True
    )
    created_on = models.DateTimeField(
        _("created on"), default=datetime.now,
        auto_now=True
    )

    def __unicode__(self):
        return self.lazy_translation_getter('title', 'News %s' % self.pk)

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")
        ordering = ['-created_on', ]
