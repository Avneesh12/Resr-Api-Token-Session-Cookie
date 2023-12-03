from django.db import models

# Create your models here.

class Emp(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=2)
    address = models.CharField(max_length=40)
    def __str__(self):
        return self.name
    