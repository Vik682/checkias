from django.urls import path
from .views import SendOTPView, ValidateOTPView
urlpatterns = [
    path('send/', SendOTPView.as_view(), name='send-otp'),
    path('validate/', ValidateOTPView.as_view(), name='validate-otp'),
]