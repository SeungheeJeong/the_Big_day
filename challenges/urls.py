from django.urls import path
from . import views

app_name = 'challenges'

urlpatterns = [
    path('create/', views.Challenge_create,
         name='create'),
    path('list/', views.ChallengeList,
         name='list'),
    path('<int:challenge_id>/', views.challengedetail,
         name='detail'),
    path('<int:challenge_id>/', views.join,
         name='join'),
]
