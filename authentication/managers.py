from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user model where the email address is the unique identifier
    and has an is_admin field to allow access to the admin app
    """
    def create_user(self, email, otp, **extra_fields):
        if not email:
            raise ValueError(("The email must be set"))
        if not otp:
            raise ValueError(("The otp must be set"))
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(False)
        user.save()
        return user

    def create_superuser(self, email, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser')is not True:
            raise ValueError('Superuser must have is_superuser=True')
        if extra_fields.get('is_staff')is not True:
            raise ValueError('Superuser must have is_staff=True')
        return self.create_user(email, is_superuser=True, **extra_fields)