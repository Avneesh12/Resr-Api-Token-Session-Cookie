from rest_framework import serializers
from django.contrib.auth.models import User

class User_seriailizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    

from .models import Student
class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'