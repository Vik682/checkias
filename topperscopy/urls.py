from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from topperscopy.views import TopperCopyView,TopperReviewView
urlpatterns = [
    path('tc/',TopperCopyView.as_view()),
    path('tr/',TopperReviewView.as_view()),
]