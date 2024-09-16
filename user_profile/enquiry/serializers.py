from rest_framework import serializers

# Create your serializers here.

# Profile of Enquiry
class EnquirySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30, required=False)
    phone_number = serializers.CharField(max_length=20, required=False)
    date_of_birth = serializers.DateField(required=False, allow_null=True)
    profile_image = serializers.ImageField( required=False)

