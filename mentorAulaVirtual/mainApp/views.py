from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Teacher
from .forms import TeacherForm

def loginUser(request):
  if request.method == 'GET':
    return render(request,'registration/login.html', {'form':AuthenticationForm()})
  else:
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is None:
      return render(request, 'registration/login.html',{'form':AuthenticationForm(), 'error':'Nombre de usuario y contraseña no coinciden'})
    else:
      login(request, user)
      return redirect('teachers') # Redirigimos a la 1º pantalla (profes)

@login_required
def clients(request):
  if request.method == 'GET':
    return render(request,'admin/clients.html', {'form':AuthenticationForm()})
  else:
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is None:
      return render(request, 'admin/clients.html',{'form':AuthenticationForm(), 'error':'Nombre de usuario y contraseña no coinciden'})
    else:
      login(request, user)
      return redirect('loginUser')

@login_required
def teachers(request):
  if request.method == 'GET':
    teachers = Teacher.objects.all()
    print(teachers)
    return render(request,'admin/teachers.html', {'form':TeacherForm(), 'teachers': teachers})
  else:
    #try:
      form = TeacherForm(request.POST)

      for key, value in dict(request.POST).items():
        print(key, '-> ', value)
      
      print(form.is_valid())
      print(form)
      newTeacher = form.save(commit=False)
      newTeacher.creator = request.user
      newTeacher.save()
      return redirect('teachers')
    #except ValueError:
    #  return render(request, 'admin/teachers.html', {'form':TeacherForm(),'error': 'Invalid data in the Teacher form'})


@login_required
def logoutUser(request):
  print("Método:",request.method )
  if request.method == 'GET':
    print("logging out")
    logout(request)
    return redirect('loginUser')