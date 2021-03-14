from django.urls import path

from . import views

urlpatterns = [
    path('analyze/', views.analyzeTweet, name='analyze')
]
