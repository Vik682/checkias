from rest_framework import serializers

# Create your serializers here.

# Profile of Superuser
class SuperuserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30, required=False)
    profile_image = serializers.ImageField( required=False)
