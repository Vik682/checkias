from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from authentication.models import User,UserToken
from authentication.serializers import UserSerializer
from mail.serializers import OTPSerializer
from mail.views import validate_otp
from rest_framework.exceptions import ValidationError
from authentication.models import USER_ROLES

#Create View here
class ValidateView(APIView):
    def post(self,request,*args,**kwargs):
        # Parse the incoming request data
        serializerotp = OTPSerializer(data=request.data)
        serializer_roleid=UserSerializer(data=request.data)
        # Check if the data is valid
        if serializerotp.is_valid() and serializer_roleid.is_valid():
            email = serializerotp.validated_data['email']
            otp = serializerotp.validated_data['otp']
            role_id = serializer_roleid.validated_data['role_id']
            try:
                validate_otp(email, otp)
                if role_id in USER_ROLES.keys():
                    if role_id in ['student','coaching','evaluator']:
                        # Assuming these IDs are for roles that create or retrieve users
                        user, created = User.objects.get_or_create(
                        email=email,
                        role=USER_ROLES[role_id])
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
            return Response(serializerotp.errors and serializer_roleid.errors, status=status.HTTP_400_BAD_REQUEST)