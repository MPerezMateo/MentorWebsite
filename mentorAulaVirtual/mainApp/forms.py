from django.forms import ModelForm
from .models import Teacher

class TeacherForm(ModelForm):
  class Meta:
    model = Teacher
    fields = ['name','surnames','phone', 'email', 'yearBirth', 'nid', 'address',
       'descr', 'studies','xpYears', 'estHours']