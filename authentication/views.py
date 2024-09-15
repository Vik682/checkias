from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from authentication.models import User,UserToken
from authentication.serializers import UserSerializer
from mail.models import OTP


role_s={
    'student': 1,
    'coaching': 2,
    'evaluator': 3,
    'reviewer': 4,
    'enquiry': 5,
    'admin': 6,
    'superuser': 7
}

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
                otp_instance = OTP.objects.get(email=email, otp=otp)
                # Check if OTP is still valid
                if otp_instance.is_valid():
                    #Check the role_id is in options
                    if role_id in ["student","coaching","evaluator","reviewer","enquiry","admin","superuser"]:
                        if role_s[role_id] in [1, 2, 3]:
                            # Assuming these IDs are for roles that create or retrieve users
                            user, created = User.objects.get_or_create(
                            email=email,
                            role=role_s[role_id])
                            # Create or retrieve user token
                            token, _ = UserToken.objects.get_or_create(user=user)
                            # Optional: Check if additional profile details are needed
                            
                            # Return response with user details and token
                            return Response({
                                'idToken': token.key,
                                    }, status=status.HTTP_200_OK)
                            
                        else:
                            try:
                                user = User.objects.get(
                                    email=email,
                                    role=role_s[role_id]
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
                else:
                    return Response({'error': 'OTP has expired'}, status=status.HTTP_400_BAD_REQUEST)
            except OTP.DoesNotExist:
                return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Return validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)