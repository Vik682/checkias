from django.db import models
from variables.optional import optional_subjects
from variables.states import states
from checkias import settings

# Create your models here.
#profile of Student
class Student(models.Model):
  medium=[('english','English'),
          ('hindi','Hindi')]
  User = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,primary_key=True)
  name = models.CharField(max_length=30,blank=True)
  phone_number = models.CharField(max_length=20,blank=True)
  attempt=models.IntegerField(null=True,default=0)
  date_of_birth = models.DateField(null = True, blank = True)
  optional=models.IntegerField(choices=optional_subjects,default=0)
  state=models.IntegerField(choices=states,default=0)
  medium = models.CharField(max_length=50,choices=medium,default='english')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  profile_image = models.ImageField(upload_to='storage/user_profile/student/profile_images/',blank=True)

  def __str__(self):
    return self.name