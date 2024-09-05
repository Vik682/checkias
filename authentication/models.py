import binascii
import os
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from user_profile.models import Student
from checkias import settings
from .managers import CustomUserManager

USER_ROLES = {
    'student': 1,
    'coaching': 2,
    'evaluator': 3,
    'reviewer': 4,
    'enquiry': 5,
    'admin': 6,
    'superuser': 7,
}

class User(AbstractUser, PermissionsMixin):
    ROLE_CHOICES = (
        (USER_ROLES['student'], _('Student')),
        (USER_ROLES['coaching'], _('Coaching')),
        (USER_ROLES['evaluator'], _('Evaluator')),
        (USER_ROLES['reviewer'], _('Reviewer')),
        (USER_ROLES['enquiry'], _('Enquiry')),
        (USER_ROLES['admin'], _('Admin')),
        (USER_ROLES['superuser'], _('Superuser')),
    )

    email = models.EmailField(
        unique=True,
        editable=False,
        verbose_name=_('Email Address'),
        primary_key=True
    )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    profile = models.OneToOneField(Student, on_delete=models.CASCADE, null=True)
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES,
        blank=True,
        null=True,
        default=USER_ROLES['student']
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    # Add related_name to avoid conflicts with the built-in User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True
    )

class UserToken(models.Model):
    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    user = models.OneToOneField(
        User,
        related_name='user_token',
        on_delete=models.CASCADE,
        verbose_name=_("User")
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        abstract = 'rest_framework.authtoken' not in settings.INSTALLED_APPS
        verbose_name = _("User Token")
        verbose_name_plural = _("User Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key








#my made
'''
import binascii
import os
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from user_profile.models import Student
from checkias import settings
from .managers import CustomUserManager

USER_ROLES = {
    'student': 1,
    'coaching': 2,
    'evaluator': 3,
    'reviewer': 4,
    'enquiry': 5,
    'admin': 6,
    'superuser': 7,
}

class User(AbstractUser, PermissionsMixin):
    ROLE_CHOICES = (
        (USER_ROLES['student'], _('Student')),
        (USER_ROLES['coaching'], _('Coaching')),
        (USER_ROLES['evaluator'], _('Evaluator')),
        (USER_ROLES['reviewer'], _('Reviewer')),
        (USER_ROLES['enquiry'], _('Enquiry')),
        (USER_ROLES['admin'], _('Admin')),
        (USER_ROLES['superuser'], _('Superuser')),
    )

    email = models.EmailField(
        unique=True,
        editable=False,
        verbose_name=_('Email Address'),
        primary_key=True
    )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    profile = models.OneToOneField(Student, on_delete=models.CASCADE, null=True)
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES,
        blank=True,
        null=True,
        default=USER_ROLES['student']
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    # Add related_name to avoid conflicts with the built-in User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True
    )

class UserToken(models.Model):
    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    user = models.OneToOneField(
        User,
        related_name='user_token',
        on_delete=models.CASCADE,
        verbose_name=_("User")
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        abstract = 'rest_framework.authtoken' not in settings.INSTALLED_APPS
        verbose_name = _("User Token")
        verbose_name_plural = _("User Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key

'''