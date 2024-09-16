from django.db import models

# Create your models here.
  
#profile of Admin
class Admin(models.Model):
  name = models.CharField(max_length=30,blank=True)
  profile_image = models.ImageField(upload_to='profile_images/',blank=True)

  def __str__(self):
    return self.name
