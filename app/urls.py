from django.urls import path
from app import views


urlpatterns = [
    path('', views.userHome, name='home'),
    path('users/', views.getUsers, name='getUsers'),
]