import json
from django.http import FileResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from user_profile.serializers import StudentSerializer
#from authentication.models import User
#from authentication.backends import UserAuthenticationBackend
from rest_framework.decorators import authentication_classes

from user_profile.models import Student
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
  
  #permission_classes = [IsAuthenticated]

  def get(self, request):
    return Response(status=200, data = '''StudentSerializer(request.user.profile).data''')

  def post(self, request):
    

    return Response(status = 200, data = { 'msg': 'success' })

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
  
  #permission_classes = [IsAuthenticated]

  def get(self, request):
    return Response(status=200, data = '''StudentSerializer(request.user.profile).data''')

  def post(self, request):
    

    return Response(status = 200, data = { 'msg': 'success' })
