from rest_framework import serializers

from user_profile.serializers import StudentSerializer

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    profile = StudentSerializer()