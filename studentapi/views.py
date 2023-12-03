import json
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import*
from .serializer import *
from rest_framework.parsers import JSONParser
import  io
# Create your views here.

@api_view(['GET'])
def emp_view(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        emp = Emp.objects.get(id=id)
        empserialize = Empserializer(emp)
        return Response(data=empserialize.data)

@api_view(['POST'])
def emp_add(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serialize = Empserializer(data=pythondata)
        if serialize.is_valid():
            serialize.save()
            res = {'msg':"Emp Added"}
            return Response(data=res)
        else:
            return Response(data=serialize.errors)


@api_view(['POST'])
def test_api(request):
    if request.method == 'POST':
        print(request.data)
        return Response("this is post method")
