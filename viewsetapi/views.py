from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from rest_framework.response import Response
from .serializer import Studentserializer

# Create your views here.

class Studentapi(viewsets.ViewSet):
    def list(self,request):
        stu = Student.objects.all()
        serializer = Studentserializer(stu,many=True)
        return Response(data=serializer.data)

    def retrieve(self,request,pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = Studentserializer(stu)
            return Response(data=serializer.data)
    
    def create(self,request):
        serializer = Studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'msz':'Student Added'})

    def update(self,request,pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = Studentserializer(stu,data=request.data)
            if serializer.is_valid():
                return Response(data={'msz':'Student Updated'})
    
    def partial_update(self,request,pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = Studentserializer(stu,data=request.data)
            if serializer.is_valid():
                return Response(data={'msz':'Student Updated'})
    
    def destroy(self,request,pk=None):
        id = pk
        if pk is not None:
            stu = Student.objects.get(id=id)
            stu.delete()
            return Response(data={'msz':'student Deleted'})


class Studentmodelviewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserializer


class StudentReadOnlyvset(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserializer