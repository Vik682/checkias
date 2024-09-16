import json
from django.http import FileResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from user_profile.serializers import StudentSerializer,EvaluatorSerializer,SuperuserSerializer,UserSerializer
from authentication.models import User
from authentication.permissions import IsEvaluator
from rest_framework import status
from rest_framework.exceptions import ValidationError
from user_profile.models import EvaluatorModel
# Create your views here.

#view of StudentProfile
class StudentProfile(APIView):
  
  #permission_classes = [IsAuthenticated]

  def get(self, request):
    return Response(status=200, data = '''StudentSerializer(request.user.profile).data''')

  def post(self, request):
    

    return Response(status = 200, data = { 'msg': 'success' })

#view of CoachingProfile
class CoachingProfile(APIView):
  
  #permission_classes = [IsAuthenticated]

  def get(self, request):
    return Response(status=200, data = '''StudentSerializer(request.user.profile).data''')

  def post(self, request):
    

    return Response(status = 200, data = { 'msg': 'success' })


#view of EvaluatorProfile
class EvaluatorProfile(APIView):
  permission_classes=[IsAuthenticated,IsEvaluator]
  def get(self, request):
    user_serializer = UserSerializer(request.user)
    
    return Response({'user': user_serializer.data,})

  def post(self, request):
        try:
            user_profile = EvaluatorModel.objects.get(User=request.user)
            serializer = EvaluatorSerializer(user_profile, data=request.data, partial=True)
        except EvaluatorModel.DoesNotExist:
            serializer = EvaluatorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(User=request.user)  # Associate the profile with the logged-in user
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()  # Update the existing profile
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#view of StudentProfile
class ReviewerProfile(APIView):
  
  #permission_classes = [IsAuthenticated]

  def get(self, request):
    return Response(status=200, data = '''StudentSerializer(request.user.profile).data''')

  def post(self, request):
    

    return Response(status = 200, data = { 'msg': 'success' })

#view of StudentProfile
class EnquiryProfile(APIView):
  
  #permission_classes = [IsAuthenticated]

  def get(self, request):
    return Response(status=200, data = '''StudentSerializer(request.user.profile).data''')

  def post(self, request):
    

    return Response(status = 200, data = { 'msg': 'success' })

#view of StudentProfile
class AdminProfile(APIView):
  
  #permission_classes = [IsAuthenticated]

  def get(self, request):
    return Response(status=200, data = '''StudentSerializer(request.user.profile).data''')

  def post(self, request):
    

    return Response(status = 200, data = { 'msg': 'success' })

#view of StudentProfile
class SuperuserProfile(APIView):
  
  permission_classes = [IsAuthenticated]

  def get(self, request):
    return Response(status=200, data = SuperuserSerializer(request.user.profile).data)

  def post(self, request):
    

    return Response(status = 200, data = { 'msg': 'success' })
