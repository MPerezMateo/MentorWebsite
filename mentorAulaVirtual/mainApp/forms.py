from django import forms
from django.forms import ModelForm
from .models import Teacher

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