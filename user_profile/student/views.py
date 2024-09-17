from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import IsStudent
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
# Create your views here.

#view of StudentProfile
class StudentProfile(APIView):
  permission_classes=[IsAuthenticated,IsStudent]
  def get(self, request):
    try:
        # Fetch the Evaluator profile for the logged-in user
        student_profile = Student.objects.get(User=request.user)
        # Serialize the data
        serializer = StudentSerializer(student_profile)
        # Return the serialized data
        return Response({'profile': serializer.data})
    except:
        return Response({'mssg': 'fail'})

  def post(self, request):
        try:
            user_profile = Student.objects.get(User=request.user)
            serializer = StudentSerializer(user_profile, data=request.data, partial=True)
        except Student.DoesNotExist:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(User=request.user)  # Associate the profile with the logged-in user
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():             
            serializer.save()  # Update the existing profile
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



