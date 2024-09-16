from django.urls import path
from user_profile.enquiry import views

urlpatterns = [
    path('', views.EnquiryProfile.as_view(), name='Enquiry profile'),
]