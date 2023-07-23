from django import forms
from django.forms import ModelForm
from django.db import models
from .models import Teacher, Client, Student, Origin


class CreateTeacherForm(ModelForm):

    class Meta:
        model = Teacher
        fields = (
            "first_name", "last_name","password", "phone", "email", "origin", "observ",
        )

class EditTeacherForm(ModelForm):
    
    class Meta:
        model = Teacher
        fields = (
            "first_name", "last_name", "phone", "email", "password", "address",
            "nid","bankName","bankAccount","bicSwift","studies","profilePic",
            "contract","origin","speciality","availability", "workingXp","estHours","prices",
            "students"
        )

class TeacherSearchForm(forms.Form):
    nameSearch = forms.CharField()
    subjSearch = forms.CharField()
    timeSearch = forms.CharField()
    studSearch = forms.CharField()


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = [
            "first_name",
            "last_name",
            "phone",
            "email",
            "address",
            "nid",
            "contract",
        ]


class ClientSearchForm(forms.Form):
    nameSearch = forms.CharField()
    studSearch = forms.CharField()

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["first_name","last_name"]


class StudentSearchForm(forms.Form):
    nameSearch = forms.CharField()
    studSearch = forms.CharField()
