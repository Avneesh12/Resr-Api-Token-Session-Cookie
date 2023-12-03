from dataclasses import field
from .models import *
from rest_framework import serializers

class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
