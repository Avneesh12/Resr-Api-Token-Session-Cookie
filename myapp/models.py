from operator import mod
from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class Personal_details(models.Model):
    address = models.CharField(max_length=40)
    student = models.OneToOneField(Student,on_delete=models.CASCADE)

class Payment_details(models.Model):
    amount = models.CharField(max_length=20)
    mode = models.CharField(max_length=20,choices=[('gpay','Gpay'),('atm','ATM'),('cash','Cash')])
    student = models.ForeignKey(Student,on_delete=models.CASCADE)

class Course_details(models.Model):
    name = models.CharField(max_length=20)
    student = models.ManyToManyField(Student)
    def __str__(self):
        return self.name

class Student_img(models.Model):
    name = models.CharField(max_length=10)
    img = models.ImageField()
    def __str__(self):
        return self.name
    
    

