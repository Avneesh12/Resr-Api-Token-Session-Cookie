from rest_framework import serializers
from myapi.models import *

class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'