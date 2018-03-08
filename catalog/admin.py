from django.contrib import admin

# Register your models here.
from .models import Prepod, Student

admin.site.register(Prepod)
admin.site.register(Student)