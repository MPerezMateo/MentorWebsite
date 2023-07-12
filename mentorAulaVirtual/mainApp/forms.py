from django import forms
from django.forms import ModelForm
from .models import Teacher, Client

class TeacherForm(ModelForm):
  class Meta:
    model = Teacher
    fields = ['admin','name','surnames','phone', 'email', 'yearBirth', 'nid', 'address',
       'descr', 'studies','xpYears', 'estHours','contract', 'profilePic']
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
    fields = ['name','surnames','phone', 'email', 'address', 'nid', 'contract',
        'descr']