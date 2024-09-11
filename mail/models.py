from django.db import models
from django.utils import timezone
from datetime import timedelta
# Create your models here.
class OTP(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    def is_valid(self):
        return self.created_at >= timezone.now() - timedelta(minutes=10)

    def __str__(self):
        return self.otp