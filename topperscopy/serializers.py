from rest_framework import serializers
from topperscopy.models import TopperCopyModel,TopperReviewModel

class TopperReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopperReviewModel
        fields = '__all__' 
        
class TopperCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = TopperCopyModel
        fields = '__all__'  # or specify fields as needed, e.g., ['field1', 'field2']