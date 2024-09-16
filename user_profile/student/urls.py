from django.urls import path
from user_profile.student import views

urlpatterns = [
    path('', views.StudentProfile.as_view(), name='Student profile'),
]