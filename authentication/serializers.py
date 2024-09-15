from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=4)
    role_id=serializers.CharField(max_length=20)
    