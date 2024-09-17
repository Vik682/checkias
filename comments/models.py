from django.db import models
from user_profile.student.models import Student
from user_profile.evaluator.models import Evaluator

# Create your models here.
class Comment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    evaluator = models.ForeignKey(Evaluator, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.student or self.evaluator} on {self.created_at}'
    
    class Meta:
        ordering = ['created_at']
