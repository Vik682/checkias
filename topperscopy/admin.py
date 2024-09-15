from django.contrib import admin
from topperscopy.models import TopperCopyModel,TopperReviewModel
# Register your models here.

class toppercopyModelAdmin(admin.ModelAdmin):
    list_display=['Name','Paper','Rank','Optional','Photo','File','Likes','Added_date']
admin.site.register(TopperCopyModel, toppercopyModelAdmin)

class topperreviewModelAdmin(admin.ModelAdmin):
    list_display=['Name','Paper','Rank','Photo','Link','Added_date']
admin.site.register(TopperReviewModel,topperreviewModelAdmin)