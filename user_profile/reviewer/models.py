from django.db import models

# Create your models here.

#profile of Reviewer
class Reviewer(models.Model):
  medium=[('english','English'),
          ('hindi','Hindi')]
  name = models.CharField(max_length=30,blank=True)
  phone_number = models.CharField(max_length=20,blank=True)
  date_of_birth = models.DateField(null = True, blank = True)
  medium = models.CharField(max_length=50,choices=medium,default='english')
  profile_image = models.ImageField(upload_to='profile_images/',blank=True)

  def __str__(self):
    return self.name

