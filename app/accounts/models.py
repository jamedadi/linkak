from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    def avatar_directory_path(self, filename):
        return 'avatars/%Y/%b/%d/{0}_{1}/'.format(self.id, filename)

    email = models.EmailField(_('email address'),unique=True)
    phone_number = models.CharField(_('phone number'), max_length=14, unique=True, null=True)
    avatar = models.ImageField(_('avatar'), upload_to=avatar_directory_path, null=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    modified_time = models.DateTimeField(_('update time'), auto_now=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_username(self):
        """Return the short name for the user."""
        return self.email

    def __str__(self):
        return self.email
