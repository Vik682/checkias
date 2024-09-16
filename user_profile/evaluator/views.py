from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import IsEvaluator
from rest_framework.response import Response
from rest_framework import status
from .models import Evaluator
from .serializers import UserSerializer,EvaluatorSerializer
# Create your views here.

#view of EvaluatorProfile
class EvaluatorProfile(APIView):
  permission_classes=[IsAuthenticated,IsEvaluator]
  def get(self, request):
    user_serializer = UserSerializer(request.user)
    
    return Response({'user': user_serializer.data,})

  def post(self, request):
        try:
            user_profile = Evaluator.objects.get(User=request.user)
            serializer = EvaluatorSerializer(user_profile, data=request.data, partial=True)
        except Evaluator.DoesNotExist:
            serializer = EvaluatorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(User=request.user)  # Associate the profile with the logged-in user
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()  # Update the existing profile
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



