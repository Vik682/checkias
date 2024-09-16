from django.contrib import admin
from .models import Coaching
# Register your models here.

#Coachings
class CoachingModelAdmin(admin.ModelAdmin):
    list_display=['name','phone_number','attempt']
admin.site.register(Coaching,CoachingModelAdmin)
