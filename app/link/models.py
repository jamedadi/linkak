from django.db import models
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext_lazy as _

from library.models import BaseModel


class Domain(BaseModel):
    ALLOW = 0
    BLOCK = 1

    STATUS = (
        (ALLOW, _('allow')),
        (BLOCK, _('block')),
    )

    host = models.CharField(max_length=255, verbose_name=_('host'))
    status = models.PositiveSmallIntegerField(
        verbose_name=_('status'), choices=STATUS, default=ALLOW
    )

    class Meta:
        verbose_name = _('Domain')
        verbose_name_plural = _('Domains')
        db_table = 'domain'


class Link(BaseModel):
    # TODO-1: create owner and foreign key to user
    domain = models.ForeignKey(Domain, related_name='links', on_delete=models.CASCADE, verbose_name=_('link'))
    slug = models.CharField(max_length=6, verbose_name=_('slug'))
    url = models.TextField(verbose_name=_('url'))
    visitor_limit = models.IntegerField(verbose_name=_('visitor_limit'), null=True)
    password = models.CharField(max_length=64, verbose_name=_('password'), null=True)
    expire_time = models.DateTimeField(verbose_name=_('expire_time'), null=True)

    @classmethod
    def generate_slug(cls):
        random_string = get_random_string(length=6)
        if cls.objects.filter(slug=random_string).exists():
            cls.generate_slug()
        return random_string

    def save_base(self, *args, **kwargs):
        self.slug = self.generate_slug()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Link')
        verbose_name_plural = _('Links')
        db_table = 'link'
