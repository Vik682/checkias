from rest_framework import serializers
from topperscopy.models import topper_copy,topper_review

class topper_copy_serializer(serializers.ModelSerializer):
    class meta:
        model=topper_copy
        fields=['Name','Paper','Rank','Optional','Photo','File','Likes','Added_date']
class topper_review_serializer(serializers.ModelSerializer):
    class meta:
        model=topper_review
        fields=['Name','Paper','Rank','Photo','Link','Added_date']