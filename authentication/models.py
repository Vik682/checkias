import binascii,os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from user_profile.models import Student,Coaching,Evaluator,Reviewer,Enquiry,Admin,Superuser
from checkias import settings
from .managers import CustomUserManager


ALLOWED_PROFILE_MODELS = {
    'student': 'Student',
    'coaching': 'Coaching',
    'evaluator': 'Evaluator',
    'reviewer': 'Reviewer',
    'enquiry': 'Enquiry',
    'admin': 'Admin',
    'superuser': 'Superuser',
}


USER_ROLES = {
    1:'student',
    2:'coaching',
    3:'evaluator',
    4:'reviewer',
    5:'enquiry',
    6:'admin',
    7:'superuser',
}



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name=('Email Address'),
        primary_key=True
    )
    role = models.IntegerField(
        choices=[(key, value.capitalize()) for key, value in USER_ROLES.items()],
        default=1
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



class UserToken(models.Model):
    key = models.CharField("Key", max_length=40, primary_key=True)
    user = models.OneToOneField(
        User,
        related_name='user_token',
        on_delete=models.CASCADE,
        verbose_name=("User")
    )
    created = models.DateTimeField("Created", auto_now_add=True)

    class Meta:
        abstract = 'rest_framework.authtoken' not in settings.INSTALLED_APPS
        verbose_name = ("User Token")
        verbose_name_plural = ("User Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
