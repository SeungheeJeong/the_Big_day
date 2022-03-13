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
    path('join/<int:challenge_id>/', views.challenger,
         name='join'),
    path('delete/<int:challenge_id>/',
         views.challenge_delete, name='delete'),
]
