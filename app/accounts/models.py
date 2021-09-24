from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager


class User(AbstractUser):

    def avatar_directory_path(self, filename):
        return 'avatars/%Y/%b/%d/{0}_{1}/'.format(self.id, filename)

    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=14, unique=True, null=True)
    avatar = models.ImageField(upload_to=avatar_directory_path, null=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()

    def __str__(self):
        return self.email
