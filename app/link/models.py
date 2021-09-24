from django.db import models
from django.utils.translation import ugettext_lazy as _

from app.library.models import BaseModel


class DomainStatus(models.IntegerChoices):
    ALLOW = 0, _('allow')
    BLOCK = 1, _('block')


class Domain(BaseModel):
    host = models.CharField(max_length=253, verbose_name=_('host'))
    status = models.PositiveSmallIntegerField(
        verbose_name=_('status'), choices=DomainStatus.choices, default=DomainStatus.ALLOW
    )

    class Meta:
        verbose_name = _('Domain')
        verbose_name_plural = _('Domains')
        db_table = 'domain'
