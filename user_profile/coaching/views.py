from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

#view of Coaching Profile
class CoachingProfile(APIView):
  
  #permission_classes = [IsAuthenticated]

  def get(self, request):
    return Response(status=200, data = '''StudentSerializer(request.user.profile).data''')

  def post(self, request):
    

    return Response(status = 200, data = { 'msg': 'success' })

