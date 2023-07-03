from django.urls import path, include
from . import views

urlpatterns = [
  path("", views.loginUser, name="loginUser"),
  path('logout/', views.logoutUser, name='logoutUser' ),
  path("clients", views.clients, name="clients")
]
