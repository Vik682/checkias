from django.contrib.auth.base_user import BaseUserManager

#Custom User Manger
class CustomUserManager(BaseUserManager):
    def create_user(self, email ,role, password=None):
        
        """
            Custom manager for the User model with email as the unique identifier.
                """
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError(('The Password field must be set'))
        if not role:
            raise ValueError(('The Role field must be set'))

        user = self.model(
            email=self.normalize_email(email),
            role=role,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,role=None, password=None):
        """
        Create and return a superuser with an email and password.
        """
        user = self.create_user(
            email,
            role=7,
            password=password,
            
        )
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user