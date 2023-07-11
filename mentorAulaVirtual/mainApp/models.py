import uuid
import os
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

class ClassLevel(models.Model):
  name = models.CharField(max_length=50, unique = True)
  price = models.DecimalField(max_digits=5, decimal_places=2)

class Subject(models.Model):
  name = models.CharField(max_length=50, unique = True) 

class SubjAndLevels(models.Model):
  
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  #numId = models.AutoField()
  subj = models.ForeignKey(Subject, on_delete = models.DO_NOTHING) # Ej: Matemáticas
  level = models.ManyToManyField(ClassLevel) # Ej: ESO

  def getname(self):
    return f"{subj} {level}"

class Availability(models.Model):
    class WeekDay(models.TextChoices):
      MONDAY = 'MON', _('Lunes')
      TUESDAY = 'TUE', _('Martes')
      WEDNESDAY = 'WED', _('Miércoles')
      THURSDAY = 'THR', _('Jueves')
      FRIDAY = 'FRI', _('Viernes')
      SATURDAY = 'SAT', _('Sábado')
      SUNDAY = 'SUN', _('Domingo')

    class Shift(models.TextChoices):
      MORNING = 'MOR', _('Mañanas')
      AFTERNOON = 'AFT', _('Tardes')
      ALL_DAY = 'A_D', _('Todo el día')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    day =  models.CharField(max_length=3, choices=WeekDay.choices) 
    shift = models.CharField(max_length=3, choices=Shift.choices) 

class BaseUser(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #numId = models.AutoField()
    name = models.CharField(max_length=50)
    surnames = models.CharField(max_length=100)
    password = models.CharField(max_length=40)
    active = models.BooleanField(default=True)
    extra = models.CharField(null=True, blank=True, max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class MonetaryUser(models.Model):
    
    phone = models.CharField(null=False, blank=False,
                             max_length=9, unique=True)
    email = models.EmailField(
        max_length=254, null=False, blank=False, unique=True)
    address = models.CharField(null=True, blank=True, max_length=255)
    nid = models.CharField(max_length=9, null=False, blank=False, unique=True)
    bankAccount = models.CharField(null=True, blank=True, max_length=40)
    bicSwift = models.CharField(null=True, blank=True, max_length=20)
    class Meta:
        abstract = True

class Student(BaseUser):
  pass

class Client(BaseUser, MonetaryUser):
    origin = models.CharField(max_length=20)
    students = models.ForeignKey(Student, on_delete=models.DO_NOTHING,)

class Teacher(BaseUser, MonetaryUser):

    def file_upload_to(self, instance=None):
        if instance:
            return os.path.join('uploads', self.nid, instance)
        return None

    yearBirth = models.PositiveSmallIntegerField(blank=True, null=True)
    
    descr = models.CharField(null=True, blank=True, max_length=255)
    studies = models.CharField(null=True, blank=True, max_length=255)
    xpYears = models.PositiveSmallIntegerField(default=0)
    estHours = models.PositiveSmallIntegerField(default=0)
    academyEmail = models.EmailField(
        null=True, blank=True, max_length=254, unique=True)
    subjects = models.ManyToManyField(Subject)
    profilePic = models.ImageField(upload_to=file_upload_to, null=True, blank=True)
    
    admin = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='administrator')
    creator = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='creator')
    category = models.CharField(null=True, blank=True, max_length=40)
    students = models.ManyToManyField(Student)
    # calendarId
    contract = models.FileField(upload_to=file_upload_to, null=True, blank=True)
    nidPhoto1 = models.ImageField(upload_to=file_upload_to, null=True, blank=True)
    nidPhoto2 = models.ImageField(upload_to=file_upload_to, null=True, blank=True)

    def __str__(self):
        return f"{self.name}, {self.nid}"


