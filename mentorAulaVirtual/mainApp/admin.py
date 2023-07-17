from django.contrib import admin
from .models import Teacher, Student, Subject, Client, Origin

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Client)
admin.site.register(Origin)