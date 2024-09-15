from django.db import models
from authentication.models import User
from checkias import settings
# Create your models here.

#profile of Student
class Student(models.Model):
  medium=[('english','English'),
          ('hindi','Hindi')]
  name = models.CharField(max_length=30,blank=True)
  phone_number = models.CharField(max_length=20,blank=True)
  attempt=models.CharField(max_length=50)
  date_of_birth = models.DateField(null = True, blank = True)
  medium = models.CharField(max_length=50,choices=medium,default='english')
  profile_image = models.ImageField(upload_to='profile_images/',blank=True)

  def __str__(self):
    return self.name
  
#profile of Coaching
class Coaching(models.Model):
  medium=[('english','English'),
          ('hindi','Hindi')]
  name = models.CharField(max_length=30,blank=True)
  phone_number = models.CharField(max_length=20,blank=True)
  attempt=models.CharField(max_length=50)
  date_of_birth = models.DateField(null = True, blank = True)
  medium = models.CharField(max_length=50,choices=medium,default='english')
  profile_image = models.ImageField(upload_to='profile_images/',blank=True)

  def __str__(self):
    return self.name

#profile of Evaluator
class EvaluatorModel(models.Model):
  medium=[('english','English'),
          ('hindi','Hindi')]
  role=[('evaluator','Evaluator'),
        ('Mentor','Mentor'),
        ('Content Creator','Content Creator')]
  languages=[
    ('hindi','Hindi'),
    ('english','English'),
  ]
  option_sub=[
    ('agriculture', 'Agriculture'),
    ('animal husbandry and veterinary science',  'Animal Husbandry and Veterinary Science'),
    ('anthropology',  'Anthropology'),
    ('botany',  'Botany'),
    ('chemistry',  'Chemistry'),
    ('civil engineering', 'Civil Engineering'),
    ('commerce & accountancy', 'Commerce & Accountancy'),
    ('economics', 'Economics'),
    ('electrical engineering',  'Electrical Engineering'),
    ('geography', 'Geography'),
    ('geology', 'Geology'),
    ('history',  'History'),
    ('law', 'Law'),
    ('management',  'Management'),
    ('mathematics',  'Mathematics'),
    ('mechanical engineering',  'Mechanical Engineering'),
    ('medical science', 'Medical Science'),
    ('philosophy',  'Philosophy'),
    ('physics',  'Physics'),
    ('political science & international relations',  'Political Science & International Relations'),
    ('psychology', 'Psychology'),
    ('public administration',  'Public Administration'),
    ('sociology',  'Sociology'),
    ('statistics', 'Statistics'),
    ('zoology',  'Zoology'),
    ('hindi literature',  'Hindi Literature'),
    ('assamese literature', 'Assamese Literature'),
    ('bengali literature',  'Bengali Literature'),
    ('bodo literature',  'Bodo Literature'),
    ('dogri literature', 'Dogri Literature'),
    ('gujarati literature',  'Gujarati Literature'),
    ('kannada literature',  'Kannada Literature'),
    ('kashmiri literature',  'Kashmiri Literature'),
    ('konkani literature',  'Konkani Literature'),
    ('maithili literature',  'Maithili Literature'),
    ('malayalam literature',  'Malayalam Literature'),
    ('manipuri literature',  'Manipuri Literature'),
    ('marathi literature',  'Marathi Literature'),
    ('nepali literature',  'Nepali Literature'),
    ('oriya literature',  'Oriya Literature'),
    ('punjabi literature',  'Punjabi Literature'),
    ('sanskrit literature',  'Sanskrit Literature'),
    ('santhali literature',  'Santhali Literature'),
    ('sindhi literature',  'Sindhi Literature'),
    ('tamil literature', 'Tamil Literature'),
    ('telugu literature',  'Telugu Literature'),
    ('urdu literature',  'Urdu Literature'),
    ('english literature',  'English Literature')
]
  User = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,primary_key=True)
  Name = models.CharField(max_length=50,blank=True)
  Phone_number = models.IntegerField(blank=True,default=0)
  date_of_birth = models.DateField(null = True, blank = True)
  Num_of_Prelims=models.IntegerField(blank=True,default=0)
  Num_of_Mains=models.IntegerField(blank=True,default=0)
  Num_of_Interviews=models.IntegerField(blank=True,default=0)
  Rank_secured=models.BooleanField(default=False)
  Medium = models.CharField(max_length=50,choices=medium,default='english')
  Profile_image = models.ImageField(upload_to='profile_images/',blank=True)
  Optional=models.CharField(max_length=90,choices=option_sub,default='Not Selected')
  Role=models.CharField(max_length=20,choices=role,blank=True)
  Evaluation_language=models.CharField(max_length=20,choices=languages,blank=True)
  Experience=models.TextField()
  Existing_std_email=models.EmailField(blank=True)
  assignment_checked=models.FileField(blank=True,upload_to='pdfs/')
  marksheet=models.FileField( upload_to='pdfs/', max_length=100,blank=True)
  def __str__(self):
    return self.Name
  
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