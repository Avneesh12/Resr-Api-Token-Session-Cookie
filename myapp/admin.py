import imp
from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Student)

@admin.register(Student,Payment_details,Personal_details,Student_img)
class Studentadmin(admin.ModelAdmin):
    pass