
from django.urls import path
from user_profile import views

urlpatterns = [
    path('student', views.StudentProfile.as_view(), name='Student profile'),
    path('coaching', views.CoachingProfile.as_view(), name='Coaching profile'),
    path('evaluator', views.EvaluatorProfile.as_view(), name='Evaluator profile'),
    path('reviewer', views.ReviewerProfile.as_view(), name='Reviewer profile'),
    path('enquiry', views.EnquiryProfile.as_view(), name='Enquiry profile'),
    path('admin', views.AdminProfile.as_view(), name='Admin'),
    path('Superuser', views.SuperuserProfile.as_view(), name='Superuser profile'),
]