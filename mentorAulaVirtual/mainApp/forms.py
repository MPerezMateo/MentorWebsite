from django import forms
from django.forms import ModelForm
from django.db import models
from .models import Teacher, Client

class TeacherForm(ModelForm):
  password = models.CharField(max_length=20, null=False, blank=False)

  class Meta:
    model = Teacher
    fields = ['admin','name','surnames','phone', 'email', 'nid', 'address',
       'profilePic', 'contract', 'descr', 'studies','xpYears', 'estHours']
       #'category'

class TeacherSearchForm(forms.Form):
  nameSearch = forms.CharField()
  subjSearch = forms.CharField()
  courseSearch = forms.CharField()
  timeSearch = forms.CharField()
  studSearch = forms.CharField()

class ClientForm(ModelForm):
  
  class Meta:
    model = Client
    fields = ['name', 'surnames','phone', 'email', 'address', 'nid', 'contract',
        'descr']
