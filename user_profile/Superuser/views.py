from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import SuperuserSerializer

# Create your views here.

#view of Superuser Profile

class SuperuserProfile(APIView):
  
  permission_classes = [IsAuthenticated]

  def get(self, request):
    return Response(status=200, data = SuperuserSerializer(request.user.profile).data)

  def post(self, request):
    

    return Response(status = 200, data = { 'msg': 'success' })
