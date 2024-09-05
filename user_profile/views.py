import json
from django.http import FileResponse
from rest_framework.views import APIView
#from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
#from user_profile.serializers import StudentSerializer
#from authentication.models import User
#from authentication.backends import UserAuthenticationBackend
from rest_framework.decorators import authentication_classes

#from user_profile.models import Student
# Create your views here.

class StudentProfile(APIView):
  #permission_classes = [IsAuthenticated]

  '''def get(self, request):
    return Response(status=200, data = StudentSerializer(request.user.profile).data)
'''
  def post(self, request):
    

    return Response(status = 200, data = { 'msg': 'success' })
