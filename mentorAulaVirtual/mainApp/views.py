from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

def loginUser(request):
  if request.method == 'GET':
    return render(request,'registration/login.html', {'form':AuthenticationForm()})
  else:
    print(request.POST['username'])
    print(request.POST['password'])
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is None:
      return render(request, 'registration/login.html',{'form':AuthenticationForm(), 'error':'Nombre de usuario y contraseña no coinciden'})
    else:
      login(request, user)
      return redirect('home')

def home(request):
  return render(request, "admin/mainAdmin.html")
