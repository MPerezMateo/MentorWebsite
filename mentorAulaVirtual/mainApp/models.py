import uuid
import os
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import  AbstractBaseUser, AbstractUser

class Origin(models.Model):
    name = models.CharField(max_length=50, unique=True)

    # url = models.CharField(max_length=50, unique = True)
    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    defaultPrice = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return self.name


class Availability(models.Model):
    class WeekDay(models.TextChoices):
        MONDAY = "MON", _("Lunes")
        TUESDAY = "TUE", _("Martes")
        WEDNESDAY = "WED", _("Miércoles")
        THURSDAY = "THR", _("Jueves")
        FRIDAY = "FRI", _("Viernes")
        SATURDAY = "SAT", _("Sábado")
        SUNDAY = "SUN", _("Domingo")

    class Shift(models.TextChoices):
        MORNING = "MOR", _("Mañanas")
        AFTERNOON = "AFT", _("Tardes")
        ALL_DAY = "A_D", _("Todo el día")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    day = models.CharField(max_length=3, choices=WeekDay.choices)
    shift = models.CharField(max_length=3, choices=Shift.choices)


class BaseUser(AbstractUser):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # numId = models.AutoField()
    # Usar Firstname y last_name de AbstractUser
    #name = models.CharField(max_length=30)
    #surnames = models.CharField(max_length=60)
    fullname = models.CharField(max_length=90)
    #Usar active
    #active = models.BooleanField(default=True)
    #Usar jonedAt
    #createdAt = models.DateTimeField(auto_now_add=True)
    observ = models.CharField(null=True, blank=True, max_length=255)

    class Meta:
      verbose_name = "BaseUser" # Aparecen mejor en el menu del admin
      verbose_name_plural = "BaseUsers"

    def save(self, *args, **kwargs):
        self.fullname = f"{self.first_name} {self.last_name}"
        super(BaseUser, self).save(*args, **kwargs)


class MonetaryUser(models.Model):
    def file_upload_to(self, instance=None):
        if instance:
            return os.path.join("uploads", self.nid, instance)
        return None

    phone = models.CharField(null=False, blank=False, max_length=9, unique=True)
    email = models.EmailField(max_length=254, null=False, blank=False, unique=True)
    address = models.CharField(null=True, blank=True, max_length=255)
    nid = models.CharField(max_length=9, null=False, blank=False, unique=True)
    bank = models.CharField(null=True, blank=True, max_length=40)
    bankAccount = models.CharField(null=True, blank=True, max_length=40)
    bicSwift = models.CharField(null=True, blank=True, max_length=20)
    contract = models.FileField(upload_to=file_upload_to, null=True, blank=True)
    dpLaw = models.BooleanField(default=False)
    validated = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Student(BaseUser):
    pass
    class Meta:
        verbose_name = "Student" # Aparecen mejor en el menu del admin
        verbose_name_plural = "Students"

class Client(BaseUser, MonetaryUser):
    origin = models.CharField(max_length=20)
    students = models.ForeignKey(
        Student,
        null=True,
        on_delete=models.DO_NOTHING,
    )
    class Meta:
        verbose_name = "Client" # Aparecen mejor en el menu del admin
        verbose_name_plural = "Clients"

class Teacher(BaseUser, MonetaryUser):
    def file_upload_to(self, instance=None):
        return MonetaryUser.file_upload_to(self, instance)

    # yearBirth = models.PositiveSmallIntegerField(blank=True, null=True)

    studies = models.CharField(null=True, blank=True, max_length=255)
    workingXp = models.PositiveSmallIntegerField(default=0)
    estHours = models.PositiveSmallIntegerField(default=0)
    academyEmail = models.EmailField(null=True, blank=True, max_length=254, unique=True)
    subjects = models.ManyToManyField(Subject, blank=True)
    profilePic = models.ImageField(upload_to=file_upload_to, null=True, blank=True)

    admin = models.ForeignKey(
        BaseUser, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="administrator"
    )
    #creator = models.ForeignKey(BaseUser, on_delete=models.DO_NOTHING, related_name="creator")
    speciality = models.CharField(null=True, blank=True, max_length=40)
    students = models.ManyToManyField(Student, blank=True)
    nidPhoto1 = models.ImageField(upload_to=file_upload_to, null=True, blank=True)
    nidPhoto2 = models.ImageField(upload_to=file_upload_to, null=True, blank=True)
    origin = models.ForeignKey(
        Origin, null=True, blank=True, on_delete=models.DO_NOTHING
    )
    prices = models.CharField(null=True, blank=True, max_length=150)
    availability = models.CharField(null=True, blank=True, max_length=150)

    class Meta:
        verbose_name = "Teacher" # Aparecen mejor en el menu del admin
        verbose_name_plural = "Teachers"

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.nid}"
