from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.loginUser, name="loginUser"),
    # Importante dejar la '/' del final para pisar el logout/ predefinido por el auth
    path('logout/', views.logoutUser, name='logoutUser'),
    path("clients", views.clients, name="clients"),
    path("teachers", views.teachers, name="teachers"),
    path('editTeacher/<uuid:teacher_id>/',
         views.editTeacher, name='editTeacher'),
    path('deleteTeacher/<uuid:teacher_id>/',
         views.deleteTeacher, name='deleteTeacher'),
]
