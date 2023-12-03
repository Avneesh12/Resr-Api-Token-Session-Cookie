from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *
# Register your models here.

@register(Student)
class Studentadmin(admin.ModelAdmin):
    pass