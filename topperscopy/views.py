from rest_framework.response import Response
from topperscopy.models import topper_copy,topper_review
from topperscopy.serializers import topper_copy_serializer,topper_review_serializer
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
class topper_copy_view(APIView):
    def post(self,request,format=None):
        serializer =topper_copy_serializer(data=request.data)
        if serializer.isvalid():
            serializer.save()
            return Response({'status':'success'})
        return Response(serializer.errors)
    def get(self,request,format=None):
        candidates=topper_copy.objects.all()
        serialize=topper_copy_serializer(candidates,many=True)
        return Response(data = topper_copy_serializer(candidates, many = True).data,status=status.HTTP_200_OK)
    
    
    
    
    
    
    
class topper_review_view(APIView):
    def post(self,request,format=None):
        serializer =topper_review_serializer(data=request.data)
        if serializer.isvalid():
            serializer.save()
            return Response({'status':'success'})
        return Response(serializer.errors)
    def get(self,request,format=None):
        candidates=topper_review.objects.all()
        serialize=topper_review_serializer(candidates,many=True)
        return Response({'status':'success'},status=status.HTTP_200_OK)