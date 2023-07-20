from django import forms
from django.forms import ModelForm
from django.db import models
from .models import Teacher, Client, Student


class TeacherForm(ModelForm):
    password = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        model = Teacher
        fields = [
            "admin",
            "first_name",
            "last_name",
            "phone",
            "email",
            "profilePic",
            "contract",
            "origin",
            "subjects",
            "speciality",
            "estHours",
            "availability",
            "prices",
            "students",
        ]


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
