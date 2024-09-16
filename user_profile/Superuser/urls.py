from django.urls import path
from user_profile.Superuser import views

urlpatterns = [
    path('', views.SuperuserProfile.as_view(), name='Superuser profile'),
]