from django.contrib import admin
from .models import Student,Coaching,Evaluator,Reviewer,Enquiry,Admin,Superuser
# Register your models here.
admin.site.register(Student)
admin.site.register(Coaching)
admin.site.register(Evaluator)
admin.site.register(Reviewer)
admin.site.register(Enquiry)
admin.site.register(Admin)
admin.site.register(Superuser)
