from django.contrib import admin
from user_profile.Admin.models import Admin
from user_profile.coaching.models import Coaching
from user_profile.enquiry.models import Enquiry
from user_profile.evaluator.models import Evaluator
from user_profile.reviewer.models import Reviewer
from user_profile.student.models import Student
from user_profile.Superuser.models import Superuser
# Register your models here.

#Admin model
admin.site.register(Admin)

#Coachings
class CoachingModelAdmin(admin.ModelAdmin):
    list_display=['name','phone_number','attempt']
admin.site.register(Coaching,CoachingModelAdmin)

#Enquiry
admin.site.register(Enquiry)

#Evaluator
class EvaluatorModelAdmin(admin.ModelAdmin):
    list_display=['Name','Phone_number']
admin.site.register(Evaluator,EvaluatorModelAdmin)

# Reviewer
admin.site.register(Reviewer)
#Students
class StudentModelAdmin(admin.ModelAdmin):
    list_display=['name','phone_number','attempt']
admin.site.register(Student,StudentModelAdmin)

# Superuser
admin.site.register(Superuser)



