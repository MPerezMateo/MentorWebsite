from django.urls import path, include
from . import views

urlpatterns = [
  path("", views.loginUser, name="login"),
  path("home", views.home, name="home"),
  
]
