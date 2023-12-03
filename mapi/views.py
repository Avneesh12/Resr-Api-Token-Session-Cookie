from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import Studentserializer
from mapi.models import Student
# Create your views here.

@api_view(['GET'])
def firstapi(request):
    return Response(data="This is First Api")

@api_view(['GET'])
def getstudent(request):
    if request.method == 'GET':
        stu = Student.objects.get(id=1)
        serializer = Studentserializer(stu)
        return Response(serializer.data)