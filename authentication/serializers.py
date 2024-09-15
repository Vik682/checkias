from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    role_id=serializers.CharField(max_length=20)
    