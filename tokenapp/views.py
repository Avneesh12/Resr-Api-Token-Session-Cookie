from venv import create
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view,permission_classes,APIView
from django.contrib.auth.models import User

from .models import Student
from .user_serializer import Student_serializer, User_seriailizer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
# Create your views here.

@api_view(['POST'])
def user_token(request):
    if request.method == 'POST':
        data = {}
        user = User_seriailizer(data=request.data)
        if user.is_valid():
            u = user.save()
            u.is_staff = True
            u.save()
            t = Token.objects.create(user=u)
            data['username'] = u.username
            data['token'] = t.key
            return Response(data=data)

        
            
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def secure_view(request):
    stu = Student.objects.all()
    stusent_serializer = Student_serializer(stu,many=True)
    return Response(data=stusent_serializer.data)


# class Get_Details(ObtainAuthToken):
#     def post(self,request,*args,**kwargs):
#         data = {}
#         serializer = User_seriailizer(data=request.data,context={'request': request})
#         if serializer.is_valid():
#             user = serializer.save()
#             token = Token.objects.get(user=user)
#             data['token'] = token.key
#             return Response(data=data)