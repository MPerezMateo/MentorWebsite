from django.urls import path, include
from . import views

urlpatterns = [
  path("", views.loginUser, name="loginUser"),
  path('logout/', views.logoutUser, name='logoutUser' ), # Importante dejar la '/' del final para pisar el logout/ predefinido por el auth
  path("clients", views.clients, name="clients"),
  path("teachers", views.teachers, name="teachers")
]
