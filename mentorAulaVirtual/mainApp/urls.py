from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.loginUser, name="loginUser"),
    # Importante dejar la '/' del final para pisar el logout/ predefinido por el auth
    path("logout/", views.logoutUser, name="logoutUser"),
    path("clients", views.clients, name="clients"),
    path("editClient/<int:client_id>/", views.editClient, name="editClient"),
    path("createClient", views.createClient, name="createClient"),
    path("deleteClient/<int:client_id>/", views.deleteClient, name="deleteClient"),
    path("teachers", views.teachers, name="teachers"),
    path("createTeacher", views.createTeacher, name="createTeacher"),
    path("editTeacher/<int:teacher_id>/", views.editTeacher, name="editTeacher"),
    path("deleteTeacher/<int:teacher_id>/", views.deleteTeacher, name="deleteTeacher"),
    path("students", views.students, name="students"),
    path("editStudent/<int:student_id>/", views.editStudent, name="editStudent"),
]
