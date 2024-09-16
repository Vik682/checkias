from django.urls import path
from user_profile.evaluator import views

urlpatterns = [
    path('', views.EvaluatorProfile.as_view(), name='Evaluator profile'),
]