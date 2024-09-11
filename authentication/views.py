import json,os
from pathlib import Path
from authentication.models import  User, UserToken
from authentication.serializers import  UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

#from google.auth.transport import requests
#from google.oauth2 import id_token
from rest_framework import exceptions


# Set the project base directory
BASE_DIR = Path(__file__).resolve().parent.parent




'''class ObtainIdTokenView(APIView):
    permission_classes = []

    def post(self, request):
        credentials = json.loads(request.body.decode('utf-8'))
        idToken = credentials.get('idToken')

        if not idToken:
            return Response(status=400, data='Email field is empty')

        try:
            decoded_token = id_token.verify_oauth2_token(
                idToken, requests.Request(), ('GOOGLE_OAUTH_CLIENT_ID'))
        except Exception:
            raise exceptions.AuthenticationFailed('Invalid ID Token')

        try:
            email = decoded_token.get("email")
            first_name = decoded_token.get("given_name").capitalize()
            last_name = decoded_token.get("family_name").capitalize()

        except Exception:
            raise exceptions.AuthenticationFailed('No such user exists')

        user, _ = User.objects.get_or_create(email=email, first_name = first_name, last_name = last_name)

        token, _ = UserToken.objects.get_or_create(user=user)

        askForDetails = True

        if user.profile:
            askForDetails = False

        return Response(status = 200, data = {
            'idToken': token.key,
            'askForDetails': askForDetails,
            'user': UserSerializer(user).data
        })'''
        
        
        
        
from rest_framework import status, views, exceptions
from rest_framework.response import Response
from .models import User, UserToken
from mail.models import OTP
from .serializers import UserSerializer
from mail.serializers import OTPSerializer

class ValidateOTPView(views.APIView):
    def post(self, request, *args, **kwargs):
        # [Ashu] python debug support
        import pdb; pdb.set_trace()
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

