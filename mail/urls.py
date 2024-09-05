from django.urls import path
from .views import CreateOTPView, ValidateOTPView
urlpatterns = [
    path('send/', CreateOTPView.as_view(), name='send-otp'),
    path('validate/', ValidateOTPView.as_view(), name='validate-otp'),
]