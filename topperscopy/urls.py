from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from topperscopy.views import topper_copy_view,topper_review_view
urlpatterns = [
    path('tc/',topper_copy_view.as_view()),
    path('tr/',topper_review_view.as_view()),
]