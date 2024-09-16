from django.db import models
from checkias import settings
from variables.optional import optional_subjects
# Create your models here.

#profile of Evaluator
class Evaluator(models.Model):
  medium=[('english','English'),
          ('hindi','Hindi')]
  role=[('evaluator','Evaluator'),
        ('Mentor','Mentor'),
        ('Content Creator','Content Creator')]
  languages=[
    ('hindi','Hindi'),
    ('english','English'),
  ]
  option_sub=optional_subjects
  User = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,primary_key=True)
  Name = models.CharField(max_length=50,blank=True)
  date_of_birth = models.DateField(null = True, blank = True)
  Phone_number = models.IntegerField(blank=True,default=0)
  Num_of_Prelims=models.IntegerField(blank=True,default=0)
  Num_of_Mains=models.IntegerField(blank=True,default=0)
  Num_of_Interviews=models.IntegerField(blank=True,default=0)
  profile_picture = models.ImageField(upload_to='storage/user_profile/evaluator/profile_pictures/', blank=True)
  Rank_secured=models.BooleanField(default=False)
  Medium = models.CharField(max_length=50,choices=medium,default='english')
  Optional=models.IntegerField(choices=option_sub,default='Not Selected')
  Role=models.CharField(max_length=20,choices=role,blank=True)
  Evaluation_language=models.CharField(max_length=20,choices=languages,blank=True)
  Experience=models.TextField(blank=True)
  Existing_std_email=models.EmailField(blank=True)
  assignment_checked=models.FileField(blank=True,upload_to='storage/user_profile/evaluator/check-pdfs/')
  marksheet=models.FileField( upload_to='storage/user_profile/evaluator/marksheet-pdfs/', max_length=100,blank=True)
  def __str__(self):
    return self.User.email
 