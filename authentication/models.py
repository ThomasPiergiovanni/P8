"""CustomUser model module.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from authentication.management.custom_user_manager import CustomUserManager


class CustomUser(AbstractUser):
    """CustomUser model class. It sa an abstarct of django user class which
    provides all user authenticaiton, login, etc. methods. Implemented in
    order to have email as identifier instead of username provided by default
    by django framework.
    """
    username = None
    email = models.EmailField(_('email address'), max_length=250, unique=True)
    first_name = models.TextField(_('first name'), max_length=100, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
