from django.urls import path
from user_profile.Admin import views

urlpatterns = [
    path('', views.AdminProfile.as_view(), name='Admin profile'),
]