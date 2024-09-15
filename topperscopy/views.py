from rest_framework.response import Response
from topperscopy.models import TopperCopyModel,TopperReviewModel
from topperscopy.serializers import TopperCopySerializer, TopperReviewSerializer
from rest_framework.views import APIView
from rest_framework import status
# from authentication.permissions import IsStudent
# from rest_framework.permissions import IsAuthenticated

class TopperCopyView(APIView):
    # permission_classes = [IsAuthenticated,IsStudent]
    def post(self, request, format=None):
        serializer = TopperCopySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        
        candidates = TopperCopyModel.objects.all()
        serializer = TopperCopySerializer(candidates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TopperReviewView(APIView):
    def post(self, request, format=None):
        serializer = TopperReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        candidates = TopperReviewModel.objects.all()
        serializer = TopperReviewSerializer(candidates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
