from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import BaseUser, Teacher, Client, Student, Subject, Origin 
from .forms import (
    TeacherForm,
    TeacherSearchForm,
    ClientForm,
    ClientSearchForm,
    StudentForm,
    StudentSearchForm,
)


def loginUser(request):
    if request.method == "GET":
        return render(
            request, "registration/login.html", {"form": AuthenticationForm()}
        )
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "registration/login.html",
                {
                    "form": AuthenticationForm(),
                    "error": "Nombre de usuario y contraseña no coinciden",
                },
            )
        else:
            login(request, user)
            # Redirigimos a la 1º pantalla (profes)
            return redirect("teachers")


@login_required
def logoutUser(request):
    print("Método:", request.method)
    if request.method == "GET":
        print("logging out")
        logout(request)
        return redirect("loginUser")


@login_required
def teachers(request):

    teacherSearch = request.GET.get("teacherSearch")
    subjSearch = request.GET.get("subjSearch")
    timeSearch = request.GET.get("timeSearch")
    studSearch = request.GET.get("studSearch")
    teachers = Teacher.objects.all()
    print(teachers[0].id )
    # Aplicamos filtros
    if teacherSearch:
        teachers = teachers.filter(first_name__contains=teacherSearch)
    if subjSearch:
        teachers = teachers.filter(subjects__name__contains=subjSearch)
    if timeSearch:
        teachers = teachers.filter(availability__contains=timeSearch)
    if studSearch:
        teachers = teachers.filter(students__name__contains=studSearch)

    if request.method == "GET":
        return render(
            request,
            "admin/teachers/teachers.html",
            {
                "searchForm": TeacherSearchForm(),
                "teachers": teachers,
                "students": Student.objects.all(),
                "staff": BaseUser.objects.values().filter(is_staff=True),
                "subjects": Subject.objects.all(),
                "origins": Origin.objects.all(),
            },
        )


@login_required
def createTeacher(request):
    if request.method == "GET":
        return render(request, "admin/teachers/createTeacher.html")

    else:
        try:
            form = TeacherForm(request.POST, request.FILES)
            for key, value in dict(request.POST).items():
                print(key, "-> ", value)
            newTeacher = form.save(commit=False)
            newTeacher.creator = request.user
            newTeacher.save()
            BaseUser = BaseUser.objects.create_user(
                username=request.POST["nid"],
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                email=request.POST["email"],
                password=request.POST["password"],
            )
            return redirect("teachers")
        except Exception as e:
            print(e)
            return render(
                request,
                "admin/teachers/teachers.html",
                {
                    "form": TeacherForm(),
                    "searchForm": TeacherSearchForm(),
                    "teachers": teachers,
                    "students": Student.objects.all(),
                    "staff": BaseUser.objects.values().filter(is_staff=True),
                    "subjects": Subject.objects.all(),
                    "origins": Origin.objects.all(),
                    "error": "Datos inválidos en el formulario de profesor. Asegúrate de que todos los campos estén cumplimentados y que el profesor no se encuentre ya en el sistema",
                },
            )


@login_required
def editTeacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    staff = BaseUser.objects.values().filter(is_staff=True)
    if request.method == "GET":
        form = TeacherForm(instance=teacher)
        return render(
            request,
            "admin/teachers/editTeacher.html",
            {"teacher": teacher, "staff": staff, "form": form},
        )

    else:
        try:
            form = TeacherForm(request.POST, instance=teacher)
            form.save()

            return redirect("teachers")
        except ValueError:
            return render(
                request,
                "admin/teachers/editTeacher.html",
                {
                    "teacher": teacher,
                    "staff": staff,
                    "form": form,
                    "error": "Datos inválidos en el formulario de profesor. Asegúrate de que todos los campos estén cumplimentados y el profesor no se encuentre en el sistema",
                },
            )


@login_required
def deleteTeacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    print(request.method)
    if request.method == "GET":
        teacher.delete()
        return redirect("teachers")
    else:
        return render(request, "admin/teachers/teacherEdit.html", {"teacher": teacher})


@login_required
def clients(request):
    teacherSearch = request.GET.get("teacherSearch")
    subjSearch = request.GET.get("subjSearch")
    timeSearch = request.GET.get("timeSearch")
    studSearch = request.GET.get("studSearch")
    clients = Client.objects.all()
    # Aplicamos filtros
    if teacherSearch:
        clients = clients.filter(name__contains=teacherSearch)
    if subjSearch:
        clients = clients.filter(subjects__name__contains=subjSearch)
    if timeSearch:
        clients = clients.filter(availability__contains=timeSearch)
    if studSearch:
        clients = clients.filter(students__name__contains=studSearch)

    if request.method == "GET":
        return render(
            request,
            "admin/clients/clients.html",
            {
                "searchForm": ClientSearchForm(),
                "clients": clients,
                "students": Student.objects.all(),
                "staff": BaseUser.objects.values().filter(is_staff=True),
                "subjects": Subject.objects.all(),
                "origins": Origin.objects.all(),
            },
        )


@login_required
def createClient(request):
    if request.method == "GET":
        return render(request, "admin/clients/createClient.html")
    else:
        try:
            form = ClientForm(request.POST, request.FILES)
            for key, value in dict(request.POST).items():
                print(key, "-> ", value)
            newClient = form.save(commit=False)
            newClient.creator = request.user
            newClient.save()
            return redirect("clients")
        except Exception as e:
            print(e)
            return render(
                request,
                "admin/clients/clients.html",
                {
                    "form": ClientForm(),
                    "searchForm": TeacherSearchForm(),
                    "teachers": teachers,
                    "students": Student.objects.all(),
                    "staff": BaseUser.objects.values().filter(is_staff=True),
                    "subjects": Subject.objects.all(),
                    "origins": Origin.objects.all(),
                    "error": "Datos inválidos en el formulario de cliente. Asegúrate de que todos los campos estén cumplimentados y que el profesor no se encuentre ya en el sistema",
                },
            )


@login_required
def editClient(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    staff = BaseUser.objects.values().filter(is_staff=True)
    if request.method == "GET":
        form = ClientForm(instance=client)
        return render(
            request,
            "admin/client/editClient.html",
            {"client": client, "staff": staff, "form": form},
        )

    else:
        try:
            form = ClientForm(request.POST, instance=client)
            form.save()

            return redirect("clients")
        except ValueError:
            return render(
                request,
                "admin/clients/editClient.html",
                {
                    "client": client,
                    "staff": staff,
                    "form": form,
                    "error": "Datos inválidos en el formulario de profesor. Asegúrate de que todos los campos estén cumplimentados y el profesor no se encuentre en el sistema",
                },
            )


@login_required
def deleteClient(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    print(request.method)
    if request.method == "GET":
        client.delete()
        return redirect("clients")
    else:
        return render(request, "admin/clients/clientEdit.html", {"client": client})


@login_required
def students(request):
    if request.method == "GET":
        return render(
            request,
            "admin/students/students.html",
            {
                "searchForm": StudentSearchForm(),
                "clients": clients,
                "students": Student.objects.all(),
                "staff": BaseUser.objects.values().filter(is_staff=True),
                "subjects": Subject.objects.all(),
                "origins": Origin.objects.all(),
            },
        )


@login_required
def createStudent(request):
    if request.method == "GET":
        return render(request, "admin/students/createStudent.html")
    else:
        try:
            form = StudentForm(request.POST, request.FILES)
            for key, value in dict(request.POST).items():
                print(key, "-> ", value)
            newStudent = form.save(commit=False)
            newStudent.creator = request.user
            newStudent.save()
            return redirect("students")
        except Exception as e:
            print(e)
            return render(
                request,
                "admin/students/students.html",
                {
                    "form": StudentForm(),
                    "searchForm": TeacherSearchForm(),
                    "teachers": teachers,
                    "students": Student.objects.all(),
                    "staff": BaseUser.objects.values().filter(is_staff=True),
                    "subjects": Subject.objects.all(),
                    "origins": Origin.objects.all(),
                    "error": "Datos inválidos en el formulario de cliente. Asegúrate de que todos los campos estén cumplimentados y que el profesor no se encuentre ya en el sistema",
                },
            )


@login_required
def editStudent(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    staff = BaseUser.objects.values().filter(is_staff=True)
    if request.method == "GET":
        form = StudentForm(instance=student)
        return render(
            request,
            "admin/students/editStudents.html",
            {"student": student, "staff": staff, "form": form},
        )

    else:
        try:
            form = StudentForm(request.POST, instance=student)
            form.save()

            return redirect("students")
        except ValueError:
            return render(
                request,
                "admin/students/editStudent.html",
                {
                    "student": student,
                    "staff": staff,
                    "form": form,
                    "error": "Datos inválidos en el formulario de profesor. Asegúrate de que todos los campos estén cumplimentados y el profesor no se encuentre en el sistema",
                },
            )


@login_required
def deleteStudent(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    print(request.method)
    if request.method == "GET":
        student.delete()
        return redirect("students")
    else:
        return render(request, "admin/student/studentEdit.html", {"student": student})
