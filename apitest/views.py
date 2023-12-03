from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapi.models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

@api_view(['GET','POST'])
def student(request,id=None):
    if request.method == 'GET':
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = Studentserializer(stu)
            return Response(data=serializer.data)
        stu = Student.objects.all()
        serializer = Studentserializer(stu,many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = Studentserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'msz':'Student Added Succesfully'})


class Studentapi(APIView):
    def get(self,request,id=None):
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = Studentserializer(stu)
            return Response(data=serializer.data)
        stu = Student.objects.all()
        serializer = Studentserializer(stu,many=True)
        return Response(data=serializer.data)
    

class Studentgenricview(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = Studentserializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class Studentgenricview2(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = Studentserializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class Studentconcretwview(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializer

class Studentconcretwview2(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializer

