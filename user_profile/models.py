from django.db import models

# Create your models here.

#profile of Student
class Student(models.Model):
  STATUS_CHOICES = [
        ('2026', '2026'),
        ('2027', '2027'),
        ('after 2027', 'After 2027'),
    ]
  medium=[('english','English'),
          ('hindi','Hindi')]
  name = models.CharField(max_length=30,blank=True)
  phone_number = models.CharField(max_length=20,blank=True)
  attempt=models.CharField(max_length=50,choices=STATUS_CHOICES,default='2026')
  date_of_birth = models.DateField(null = True, blank = True)
  medium = models.CharField(max_length=50,choices=medium,default='english')
  profile_image = models.ImageField(upload_to='profile_images/',blank=True)
  courseenroll=models.CharField(max_length=1000,blank=True)

  def __str__(self):
    return self.name
  
#profile of Coaching
class Coaching(models.Model):
  STATUS_CHOICES = [
        ('2026', '2026'),
        ('2027', '2027'),
        ('after 2027', 'After 2027'),
    ]
  medium=[('english','English'),
          ('hindi','Hindi')]
  name = models.CharField(max_length=30,blank=True)
  phone_number = models.CharField(max_length=20,blank=True)
  attempt=models.CharField(max_length=50,choices=STATUS_CHOICES,default='2026')
  date_of_birth = models.DateField(null = True, blank = True)
  medium = models.CharField(max_length=50,choices=medium,default='english')
  profile_image = models.ImageField(upload_to='profile_images/',blank=True)
  courseenroll=models.CharField(max_length=1000,blank=True)

  def __str__(self):
    return self.name

#profile of Evaluator
class Evaluator(models.Model):
  medium=[('english','English'),
          ('hindi','Hindi')]
  name = models.CharField(max_length=30,blank=True)
  phone_number = models.CharField(max_length=20,blank=True)
  date_of_birth = models.DateField(null = True, blank = True)
  medium = models.CharField(max_length=50,choices=medium,default='english')
  profile_image = models.ImageField(upload_to='profile_images/',blank=True)

  def __str__(self):
    return self.name
  
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


#profile of Enquiry
class Enquiry(models.Model):
  name = models.CharField(max_length=30,blank=True)
  phone_number = models.CharField(max_length=20,blank=True)
  date_of_birth = models.DateField(null = True, blank = True)
  profile_image = models.ImageField(upload_to='profile_images/',blank=True)

  def __str__(self):
    return self.name
  
  
#profile of Admin
class Admin(models.Model):
  name = models.CharField(max_length=30,blank=True)
  profile_image = models.ImageField(upload_to='profile_images/',blank=True)

  def __str__(self):
    return self.name


#profile of Superuser
class Superuser(models.Model):
  name = models.CharField(max_length=30,blank=True)
  profile_image = models.ImageField(upload_to='profile_images/',blank=True)

  def __str__(self):
    return self.name