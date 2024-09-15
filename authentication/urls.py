from django.contrib import admin
from django.urls import path,include
from .views import ValidateView

urlpatterns = [
    path('validate/', ValidateView.as_view(), name='validate-otp'),
    ]