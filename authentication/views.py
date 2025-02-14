from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from authentication.models import User,UserToken
from authentication.serializers import UserSerializer
from mail.views import validate_otp
from rest_framework.exceptions import ValidationError
from authentication.models import USER_ROLES
from django.db import IntegrityError


#Create View here
class ValidateView(APIView):
    def post(self,request,*args,**kwargs):
        # Parse the incoming request data
        serializer = UserSerializer(data=request.data)
        
        # Check if the data is valid
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            role_id = serializer.validated_data['role_id']
            try:
                validate_otp(email, otp)  # Validate OTP
                if role_id in USER_ROLES.keys():
                    if role_id in ['student','coaching','evaluator','reviewer','enquiry']:
                        # Try to create or retrieve the user
                        try:
                            # Assuming these IDs are for roles that create or retrieve users
                            user, created = User.objects.get_or_create(
                            email=email,
                            role=USER_ROLES[role_id])
                            # Create or retrieve user token
                            token, _ = UserToken.objects.get_or_create(user=user)
                            # Return response with user details and token
                            return Response({
                                'idToken': token.key,
                                    }, status=status.HTTP_200_OK)
                        except IntegrityError:
                            # Handle IntegrityError if email already exists
                            return Response({
                                'error': 'A user with this email already exists.'
                            }, status=status.HTTP_400_BAD_REQUEST)
                                                    
                    else:
                        try:
                            user = User.objects.get(
                                email=email,
                                role=USER_ROLES(role_id)
                                            )
                            # Create or retrieve user token
                            token, _ = UserToken.objects.get_or_create(user=user)
                                
                            # Return response with user details and token
                            return Response({
                                'idToken': token.key,
                                    }, status=status.HTTP_200_OK)
                        except :
                            return Response({'error': 'Invalid Login'}, status=status.HTTP_400_BAD_REQUEST)
                        
                else:
                    return Response({'error': 'Invalid Role_id'}, status=status.HTTP_400_BAD_REQUEST)
            except ValidationError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Return validation errors
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)