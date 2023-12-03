from functools import partial
from django.shortcuts import render
from rest_framework.views import APIView

from classapi.models import Student
from .serializer import *
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import *


# Create your views here.

class Classview(APIView):
    def get(self,request,id=None):
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = Studentserializer(stu)
            return Response(data= serializer.data)
        stu = Student.objects.all()
        serializer = Studentserializer(stu,many=True)
        return Response(data=serializer.data)
    
    def post(self,request):
        serializer = Studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'msz':'Student Added'})
    
    def put(self,request,id=None):
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = Studentserializer(stu,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data={'msz':'Student Updated fully'})

    def patch(self,request,id=None):
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = Studentserializer(stu,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data={'msz':'Student Updated Partially'})

    def delete(self,request,id=None):
        if id is not None:
            stu = Student.objects.get(id=id)
            stu.delete()
            return Response(data={'msz':'Student Deleted'})


class Mixinview(GenericAPIView,ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = Studentserializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    

class Mixinview2(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = Studentserializer
    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class Concreteapiview(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializer


class Concreteapiview(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializer