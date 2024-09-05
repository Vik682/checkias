from django.db import models

# Create your models here.
# toppers copy models.
class topper_copy(models.Model):
    Name=models.CharField(max_length=25)
    Paper=models.CharField(max_length=50)
    Rank=models.PositiveIntegerField()
    Optional=models.CharField(max_length=25)
    Photo=models.ImageField(upload_to='toppers/photo',null=True)
    File=models.FileField(upload_to='toppers/copy')
    Likes=models.PositiveIntegerField()
    Added_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return 'MyModel: {}'.format(self.Name)
    
class topper_review(models.Model):
    Name=models.CharField(max_length=25)
    Paper=models.CharField(max_length=50)
    Rank=models.PositiveIntegerField()
    Photo=models.ImageField(upload_to='toppers/photo',null=True)
    Link=models.URLField(null=True)
    Added_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return 'MyModel: {}'.format(self.Name)