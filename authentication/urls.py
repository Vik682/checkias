from django.contrib import admin
from django.urls import path,include
from .views import ValidateOTPView

urlpatterns = [
    path('validate/', ValidateOTPView.as_view(), name='validatae-otp'),
    ]