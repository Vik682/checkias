from django.urls import path,include
# Urlspatterns
urlpatterns = [
    path('student', include('user_profile.student.urls')),
    path('coaching', include('user_profile.coaching.urls')),
    path('evaluator',include('user_profile.evaluator.urls')),
    path('reviewer', include('user_profile.reviewer.urls')),
    path('enquiry', include('user_profile.enquiry.urls')),
    path('admin', include('user_profile.Admin.urls')),
    path('Superuser', include('user_profile.Superuser.urls')),
]