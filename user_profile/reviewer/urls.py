from django.urls import path
from user_profile.reviewer import views

urlpatterns = [
    path('', views.ReviewerProfile.as_view(), name='Reviewer profile'),
]