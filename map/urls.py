from django.urls import path
from . import views

app_name = 'map'

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.map_create, name="create"),
]
