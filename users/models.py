from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['first_name']

    objects = CustomUserManager()

    @property
    def get_token(self):
        token = Token.objects.get(user_id=self.pk)
        return f"{token}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)
