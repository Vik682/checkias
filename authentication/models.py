import binascii,os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from checkias import settings
from authentication.managers import CustomUserManager

USER_ROLES = {
    'student':1,
    'coaching':2,
    'evaluator':3,
    'reviewer':4,
    'enquiry':5,
    'admin':6,
    'superuser':7,
}



class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES=(
        (USER_ROLES['student'],'Student'),
        (USER_ROLES['coaching'],'Coaching'),
        (USER_ROLES['evaluator'],'Evaluator'),
        (USER_ROLES['reviewer'],'Reviewer'),
        (USER_ROLES['enquiry'],'Enquiry'),
        (USER_ROLES['admin'],'Admin'),
        (USER_ROLES['superuser'],'Superuser'),
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name=('Email Address'),
        primary_key=True
    )
    role = models.IntegerField(
        choices=ROLE_CHOICES
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
        abstract = False #rest_framework.authtoken' not in settings.INSTALLED_APPS //change if cause any problem 
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
