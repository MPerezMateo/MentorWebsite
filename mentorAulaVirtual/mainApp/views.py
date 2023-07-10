from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Teacher
from .forms import TeacherForm, TeacherSearchForm


def loginUser(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'registration/login.html', {'form': AuthenticationForm(), 'error': 'Nombre de usuario y contraseña no coinciden'})
        else:
            login(request, user)
            # Redirigimos a la 1º pantalla (profes)
            return redirect('teachers')


@login_required
def clients(request):
    if request.method == 'GET':
        return render(request, 'admin/clients.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'admin/clients.html', {'form': AuthenticationForm(), 'error': 'Nombre de usuario y contraseña no coinciden'})
        else:
            login(request, user)
            return redirect('loginUser')


@login_required
def teachers(request):
    teachers = Teacher.objects.all()
    staff = User.objects.values().filter(is_staff=True)
    searchName = request.GET.get("nameSearch")
    if searchName:
      teachers = teachers.filter(name = searchName)
    if request.method == 'GET':
        return render(request, 'admin/teachers.html', {'form': TeacherForm(), 'searchForm': TeacherSearchForm(), 'teachers': teachers, 'staff': staff})
    else:
        try:
            form = TeacherForm(request.POST, request.FILES)
            for key, value in dict(request.POST).items(): print(key, '-> ', value)
            newTeacher = form.save(commit=False)
            newTeacher.creator = request.user
            newTeacher.save()
            return redirect('teachers')
        except Exception as e:
            print(e)
            return render(request, 'admin/teachers.html', {'form': form, 'staff': staff, 'teachers': teachers, 'error': 'Datos inválidos en el formulario de profesor. Asegúrate de que todos los campos estén cumplimentados y el profesor no se encuentre en el sistema'})


@login_required
def logoutUser(request):
    print("Método:", request.method)
    if request.method == 'GET':
        print("logging out")
        logout(request)
        return redirect('loginUser')


@login_required
def editTeacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    staff = User.objects.values().filter(is_staff=True)
    if request.method == 'GET':
        form = TeacherForm(instance=teacher)
        return render(request, 'admin/teacherEdit.html', {'teacher': teacher,'staff':staff, 'form': form})

    else:
        try:
            form = TeacherForm(request.POST, instance=teacher)
            form.save()
            
            return redirect('teachers')
        except ValueError:
            return render(request, 'admin/teacherEdit.html', {'teacher': teacher,'staff':staff, 'form': form, 'error': 'Datos inválidos en el formulario de profesor. Asegúrate de que todos los campos estén cumplimentados y el profesor no se encuentre en el sistema'})


@login_required
def deleteTeacher(request, teacher_id):
    print("AAAA")

    teacher = get_object_or_404(Teacher, pk=teacher_id)
    print(request.method)
    if request.method == 'GET':
        teacher.delete()
        return redirect('teachers')
    else:
        return render(request, 'admin/teacherEdit.html', {'teacher': teacher})
