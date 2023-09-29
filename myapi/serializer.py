from rest_framework import serializers
from .models import *


class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

# class Student_serializer(serializers.Serializer):
#     name = serializers.CharField()
#     age = serializers.CharField()
#     address = serializers.CharField()

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)