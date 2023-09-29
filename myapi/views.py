from functools import partial
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def get_student_api(request,id=None):
    if request.method == 'GET':
        if id == None:
            stu = Student.objects.all()
            stu_serializer = Student_serializer(stu,many=True)
            return Response(data=stu_serializer.data)
        else:
            stu = Student.objects.get(id=id)
            stu_serializer = Student_serializer(stu)
            return Response(data=stu_serializer.data)
    elif request.method == 'POST':
        stu_data = request.data
        stu_serializer = Student_serializer(data=stu_data)
        if stu_serializer.is_valid():
            stu_serializer.save()
            return Response(data={'msg':'Student ADded Succesfully'})
        else:
            return Response(data={'msz':stu_serializer.errors})
    elif request.method == 'PUT':
        stu = Student.objects.get(id=id)
        stu_data = request.data
        stu_serializer = Student_serializer(stu,data=stu_data)
        if stu_serializer.is_valid():
            stu_serializer.save()
            return Response(data={'msg':'Student Updated Succesfully'})
        else:
            return Response(data={'msz':stu_serializer.errors})
    elif request.method == 'PATCH':
        stu = Student.objects.get(id=id)
        stu_data = request.data
        stu_serializer = Student_serializer(stu,data=stu_data,partial=True)
        if stu_serializer.is_valid():
            stu_serializer.save()
            return Response(data={'msg':'Student Partially Updated Succesfully'})
        else:
            return Response(data={'msz':stu_serializer.errors})
    elif request.method == 'DELETE':
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response(data={'msz':'Student Deleted Succesfully'})


class Student_api(APIView):
    def get(self,request,id=None):
        if id == None:
            stu = Student.objects.all()
            stu_serializer = Student_serializer(stu,many=True)
            return Response(data=stu_serializer.data)
        else:
            stu = Student.objects.get(id=id)
            stu_serializer = Student_serializer(stu)
            return Response(data=stu_serializer.data)
    def post(self,request):
        stu = request.data
        stu_serializer = Student_serializer(data=stu)
        if stu_serializer.is_valid():
            stu_serializer.save()
            return Response(data={'msz':'Student Added Succesfully'})
        else:
            return Response(data={'msz':stu_serializer.errors})
    def put(self,request,id):
        stu = Student.objects.get(id=id)
        stu_serializer = Student_serializer(stu,data=request.data)
        if stu_serializer.is_valid():
            stu_serializer.save()
            return Response(data={'msz':'Student Updated'})
        else:
            return Response(data={'msz':stu_serializer.errors})
    def patch(self,request,id):
        stu = Student.objects.get(id=id)
        stu_serializer = Student_serializer(stu,data=request.data,partial=True)
        if stu_serializer.is_valid():
            stu_serializer.save()
            return Response(data={'msz':'Student Updated Partially'})
        else:
            return Response(data={'msz':stu_serializer.errors})
    def delete(self,request,id):
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response(data={'msz':'Student Deleted Succesfully'})


class Genric_student_view(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = Student_serializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class Generic_student_api_view2(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = Student_serializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    

class Concrete_view1(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Student_serializer

class Concrete_view2(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = Student_serializer






from rest_framework import viewsets

class Student_viewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Student_serializer

class Student_viewset(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Student_serializer