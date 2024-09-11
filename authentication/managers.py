from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom manager for the User model with email as the unique identifier.
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError(_('The Email field must be set'))
        if not password:
            raise ValueError(_('The Password field must be set'))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hash the password before saving
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        # Ensure default values for superuser fields
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        # Remove superuser-specific fields from extra_fields to avoid conflicts
        is_superuser = extra_fields.pop('is_superuser', None)
        is_staff = extra_fields.pop('is_staff', None)
        is_active = extra_fields.pop('is_active', None)

        # Create the user with the adjusted extra fields
        user = self.create_user(email, password, **extra_fields)
        
        # Set superuser-specific fields
        user.is_superuser = is_superuser
        user.is_staff = is_staff
        user.is_active = is_active
        user.save(using=self._db)

        return user
