import json,os
from pathlib import Path
from authentication.models import User, UserToken
from authentication.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from mail.models import OTP
from mail.serializers import OTPSerializer
from user_profile.models import Student, Coaching, Evaluator, Reviewer, Enquiry, Admin, Superuser
from authentication.models import USER_ROLES
from django.contrib.contenttypes.models import ContentType  # Make sure this is imported
# Set the project base directory
BASE_DIR = Path(__file__).resolve().parent.parent

class ValidateView(APIView):
    def post(self, request, *args, **kwargs):
        # Parse the incoming request data
        serializer = OTPSerializer(data=request.data)
        
        # Validate the serializer data
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            role_id = request.data.get('role_id')  # Get the role_id from request data
            
            if role_id not in USER_ROLES.values():
                return Response({'error': 'Invalid role ID'}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                # Retrieve OTP instance based on email and OTP
                otp_instance = OTP.objects.get(email=email, otp=otp)
                
                # Check if OTP is still valid
                if otp_instance.is_valid():
                    # Determine profile type based on role_id
                    profile_type = next((key for key, value in USER_ROLES.items() if value == role_id), None)
                    
                    if profile_type is None:
                        return Response({'error': 'Invalid role ID'}, status=status.HTTP_400_BAD_REQUEST)
                    
                    profile_model = {
                        'student': Student,
                        'coaching': Coaching,
                        'evaluator': Evaluator,
                        'reviewer': Reviewer,
                        'enquiry': Enquiry,
                        'admin': Admin,
                        'superuser': Superuser,
                    }[profile_type]
                    
                    # Retrieve or create the profile instance
                    profile, profile_created = profile_model.objects.get_or_create()  # Customize as needed
                    
                    # Retrieve or create user based on email
                    user, created = User.objects.get_or_create(
                        email=email,
                        defaults={
                            'profile_content_type': ContentType.objects.get_for_model(profile),
                            'profile_id': profile.id,
                            'profile_type': profile_type
                        }
                    )
                    
                    # Create or retrieve user token
                    token, _ = UserToken.objects.get_or_create(user=user)
                    
                    # Optional: Check if additional profile details are needed
                    ask_for_details = not user.profile
                    
                    # Return response with user details and token
                    return Response({
                        'idToken': token.key,
                        'askForDetails': ask_for_details,
                        'user': UserSerializer(user).data
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'OTP has expired'}, status=status.HTTP_400_BAD_REQUEST)
            except OTP.DoesNotExist:
                return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Return validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
