from re import S
from turtle import update
from venv import create
from django.shortcuts import render
from .studentserializer import *
from .models import *
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView


# class Studentlist(GenericAPIView,ListModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = Studentserializer

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

# class Studentcreate(GenericAPIView,CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = Studentserializer
    
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)


# class Studentretrive(GenericAPIView,RetrieveModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = Studentserializer
    
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)

# class Studentupdate(GenericAPIView,UpdateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = Studentserializer

#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)

# class Studentdelete(GenericAPIView,DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = Studentserializer
    
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)



# class Studentview1(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = Studentserializer

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
    
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)



# class Studentview2(GenericAPIView,ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = Studentserializer
    
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)

#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)

#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)



#####################COncrete API##############################

class Studentlistapiview(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializer

