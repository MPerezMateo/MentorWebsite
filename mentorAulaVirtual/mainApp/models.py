import uuid
import os
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    surnames = models.CharField(max_length=100)


class Teacher(models.Model):

    def file_upload_to(self, instance=None):
        if instance:
            return os.path.join('uploads', self.nid, instance)
        return None

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    surnames = models.CharField(max_length=100)
    password = models.CharField(max_length=40)
    phone = models.CharField(null=False, blank=False,
                             max_length=9, unique=True)
    email = models.EmailField(
        max_length=254, null=False, blank=False, unique=True)
    yearBirth = models.PositiveSmallIntegerField(blank=True, null=True)
    nid = models.CharField(max_length=9, null=False, blank=False, unique=True)
    address = models.CharField(null=True, blank=True, max_length=255)
    descr = models.CharField(null=True, blank=True, max_length=255)
    studies = models.CharField(null=True, blank=True, max_length=255)
    xpYears = models.PositiveSmallIntegerField(default=0)
    estHours = models.PositiveSmallIntegerField(default=0)
    academyEmail = models.EmailField(
        null=True, blank=True, max_length=254, unique=True)
    subjects = models.CharField(null=True, blank=True, max_length=150)
    bankAccount = models.CharField(null=True, blank=True, max_length=40)
    bicSwift = models.CharField(null=True, blank=True, max_length=20)
    extra = models.CharField(null=True, blank=True, max_length=255)
    profilePic = models.ImageField(upload_to=file_upload_to, null=True, blank=True)
    password = models.CharField(null=True, blank=True, max_length=40)
    active = models.BooleanField(default=True)
    admin = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='administrator')
    createdAt = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='creator')
    category = models.CharField(null=True, blank=True, max_length=40)
    students = models.ManyToManyField(Student)
    # calendarId
    contract = models.FileField(upload_to=file_upload_to, null=True, blank=True)
    nidPhoto1 = models.ImageField(upload_to=file_upload_to, null=True, blank=True)
    nidPhoto2 = models.ImageField(upload_to=file_upload_to, null=True, blank=True)

    def __str__(self):
        return f"{self.id}, {self.name}, {self.nid}"

    