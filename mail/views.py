from django.utils.crypto import get_random_string
from rest_framework import status, views
from rest_framework.response import Response
from .models import OTP
from .serializers import OTPSerializer

# Create your views here.





import smtplib

# Email account credentials
smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = ''#fill sender code
password = ''#fill sender passcode
sender_email = ''

# Email content

sender_email = ''
subject = 'Verif. otp-Checkias'



# Connect to the server and send email
def sendmail(receiver_email,body):
    try:
        message = f"""
        {body}
        """
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(username, password)
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        return "not-sent"
    finally:
        server.quit()


# otp/views.py



class SendOTPView(views.APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email'.lower())
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        otp = get_random_string(length=4, allowed_chars='1234567890')
        # Send OTP email
        sendmail(receiver_email=email,body=f'Your OTP code is {otp}. It is valid for 10 minutes.')
        OTP.objects.create(email=email, otp=otp)
        
        return Response({'message': f'OTP sent successfully'}, status=status.HTTP_200_OK)

class ValidateOTPView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = OTPSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            
            try:
                otp_instance = OTP.objects.get(email=email, otp=otp)
                if otp_instance.is_valid():
                    return Response({'message': 'OTP is valid'}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'OTP has expired'}, status=status.HTTP_400_BAD_REQUEST)
            except OTP.DoesNotExist:
                return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
