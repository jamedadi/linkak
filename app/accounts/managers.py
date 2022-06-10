import re

from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    @classmethod
    def normalize_phone_number(cls, phone_number:str):
        """ check valid phone number with regular expressions"""

        pattern = re.compile(r"^(\\+98|0|0098)?9\\d{9}$")
        if not re.fullmatch(pattern, phone_number):
            raise ValueError('Phone number must be valid')

        return phone_number

    def create_user(self, email, phone_number=None, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have email address')

        user = self.model(email=self.normalize_email(email),
                          phone_number=self.normalize_phone_number(phone_number) if phone_number is not None else None,
                          **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, phone_number=None):
        user = self.create_user(email, phone_number, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
