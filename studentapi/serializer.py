from rest_framework import serializers
from .models import *

class Empserializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    age = serializers.CharField(max_length=2)
    address = serializers.CharField(max_length=40)

    def create(self, validated_data):
        return Emp.objects.create(**validated_data)