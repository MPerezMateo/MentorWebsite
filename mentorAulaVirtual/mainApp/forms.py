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
            "name",
            "surnames",
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
            "name",
            "surnames",
            "phone",
            "email",
            "address",
            "nid",
            "contract",
            "descr",
        ]


class ClientSearchForm(forms.Form):
    nameSearch = forms.CharField()
    studSearch = forms.CharField()


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["name", "surnames", "descr"]


class StudentSearchForm(forms.Form):
    nameSearch = forms.CharField()
    studSearch = forms.CharField()
