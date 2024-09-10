import json,os
from pathlib import Path
from authentication.models import  User, UserToken
from authentication.serializers import  UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, exceptions
from rest_framework.response import Response
from mail.models import OTP
from mail.serializers import OTPSerializer


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
            
            try:
                # Retrieve OTP instance based on email and OTP
                otp_instance = OTP.objects.get(email=email, otp=otp)
                
                # Check if OTP is still valid
                if otp_instance.is_valid():
                    # Retrieve or create user based on email
                    user, created = User.objects.get_or_create(email=email)
                    
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

