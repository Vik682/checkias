from django.db import models

# Create your models here.

#profile of Enquiry
class Enquiry(models.Model):
  name = models.CharField(max_length=30,blank=True)
  phone_number = models.CharField(max_length=20,blank=True)
  date_of_birth = models.DateField(null = True, blank = True)
  profile_image = models.ImageField(upload_to='profile_images/',blank=True)

  def __str__(self):
    return self.name