from functools import partial
from urllib import request
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from funapi.models import Student
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

# @api_view(['GET','POST'])
# def api_get(request):
#     if request.method == 'GET':
#         stu = Student.objects.all()
#         serializer = Studentserializer(stu,many=True)
#         return Response(data=serializer.data)
#     elif request.method == 'POST':
#         id = request.data.get('id')
#         stu = Student.objects.get(id=id)
#         serializer = Studentserializer(stu)
#         return Response(serializer.data)

# @api_view(['POST','PUT','DELETE','PATCH'])
# def api_post(request):
#     if request.method == 'POST':
#         serializer = Studentserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data={'msg':"STudent Data Added"})
#         else:
#             return Response(data=serializer.errors)
#     elif request.method == 'PUT':
#         id = request.data.get('id')
#         stu = Student.objects.get(id=id)
#         serializer = Studentserializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data={'msz':'Student Details are Updated '})
#         else:
#             return Response(data={'msg':serializer.errors})
#     elif request.method == 'DELETE':
#         id = request.data.get('id')
#         stu = Student.objects.get(id=id) 
#         stu.delete()
#         return Response(data={'msz':"deleted"})
#     elif request.method == 'PATCH':
#         id = request.data.get('id')
#         stu = Student.objects.get(id=id)
#         serializer = Studentserializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data={'msg':"Student details partial Updated"})
#         else:
#             return Response(data={'msz':serializer.errors})



# @api_view(['GET'])
# def api_get(request,id=None):
#     if id is not None:
#         id = id
#         stu = Student.objects.get(id=id)
#         serializer = Studentserializer(stu)
#         return Response(data=serializer.data)
#     stu = Student.objects.all()
#     serializer = Studentserializer(stu,many=True)
#     return Response(data=serializer.data)


class Studentview(APIView):
    def get(self,request,id=None,format=None):
        id = id
        if id is not None:
            stu = Student.objects.get(id=id)
            serialize = Studentserializer(stu)
            return Response(data=serialize.data)
        stu = Student.objects.all()
        serialize = Studentserializer(stu,many=True)
        return Response(data=serialize.data)

    def post(self,request,format=None):
        serialize = Studentserializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(data={'msg':'Student Added'})
    
    def delete(self,request,id=None,format=None):
        id = id
        if id is not None:
            stu = Student.objects.get(id=id)
            stu.delete()
            return Response(data={'msz':'STudent Data Deleted'})

    def put(self,request,id=None,format=None):
        id = id
        stu = Student.objects.get(id=id)
        serialize = Studentserializer(stu,data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(data={'msz':'Student Data Fully Updated'})
        return Response(data={'msz':serialize.errors},status=status.HTTP_400_BAD_REQUEST)
        
    
    def patch(self,request,id=None,format=None):
        id = id
        stu = Student.objects.get(id=id)
        serialize = Studentserializer(stu,data=request.data,partial=True)
        if serialize.is_valid():
            serialize.save()
            return Response(data={'msz':'Student Data Partially Updated'})
    
