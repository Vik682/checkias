from rest_framework import serializers

# Create your serializers here.
 
# Profile of Reviewer
class ReviewerSerializer(serializers.Serializer):
    MEDIUM_CHOICES = [
        ('english', 'English'),
        ('hindi', 'Hindi'),
    ]
    name = serializers.CharField(max_length=30, required=False)
    phone_number = serializers.CharField(max_length=20, required=False)
    date_of_birth = serializers.DateField(required=False, allow_null=True)
    medium = serializers.ChoiceField(choices=MEDIUM_CHOICES, default='english')
    profile_image = serializers.ImageField( required=False)

