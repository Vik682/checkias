
from django.urls import path
from user_profile import views

urlpatterns = [
    path('student', views.StudentProfile.as_view(), name='student_profile'),
    path('coaching', views.CoachingProfile.as_view(), name='coaching_profile'),
    path('evaluator', views.EvaluatorProfile.as_view(), name='evaluator_profile'),
    path('reviewer', views.ReviewerProfile.as_view(), name='reviewer_profile'),
    path('enquiry', views.EnquiryProfile.as_view(), name='enquiry_profile'),
    path('admin', views.AdminProfile.as_view(), name='admin'),
    path('Superuser', views.SuperuserProfile.as_view(), name='Superuser_profile'),
]