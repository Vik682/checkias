from django.urls import path
from user_profile.coaching import views

urlpatterns = [
    path('', views.CoachingProfile.as_view(), name='Coaching profile'),
]