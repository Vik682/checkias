from rest_framework import serializers
from authentication.models import USER_ROLES

class UserSerializer(serializers.Serializer):
    role_id=serializers.CharField(max_length=20)
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    def validate_role_id(self, value):
        '''Ensure the role_id is valid.'''
        if value not in USER_ROLES:
            raise serializers.ValidationError("Invalid role_id")
        return value

    