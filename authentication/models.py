import binascii,os
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from user_profile.models import Student
from checkias import settings


USER_ROLES={
    'student': 1,
    'coaching':2,
    'evaluator': 3,
    'reviewer': 4,
    'enquiry': 5,
    'admin': 6,
    'superuser': 7,
}

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    # These fields tie to the roles!
    ROLE_CHOICES = (
        (USER_ROLES['student'], 'Student'),
        (USER_ROLES['coaching'], 'Coaching'),
        (USER_ROLES['evaluator'], 'Evaluator'),
        (USER_ROLES['reviewer'], 'Reviewer'),
        (USER_ROLES['enquiry'], 'Enquiry'),
        (USER_ROLES['admin'], 'Admin'),
        (USER_ROLES['superuser'], 'Superuser'),
    )

    # Roles created here
    email = models.EmailField(unique=True,editable=False,verbose_name='Public identifier',primary_key=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    profile = models.OneToOneField(Student, on_delete=models.CASCADE, null = True)
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, blank=True, null=True, default=1)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class UserToken(models.Model):
    """
    The staff authorization token model.
    """
    key = models.CharField(("Key"), max_length=40, primary_key=True)
    user = models.OneToOneField(
        User, related_name='id_token',
        on_delete=models.CASCADE, verbose_name=("User")
    )
    created = models.DateTimeField(("Created"), auto_now_add=True)

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