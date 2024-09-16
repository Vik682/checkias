from django.contrib import admin
from .models import Student
# Register your models here.
#Students
class StudentModelAdmin(admin.ModelAdmin):
    list_display=['name','phone_number','attempt']
admin.site.register(Student,StudentModelAdmin)
