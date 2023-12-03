from django.urls import path
from .views import *

urlpatterns = [
    # path('stuapi/',Studentlist.as_view()),
    # path('stuapi/',Studentcreate.as_view()),
    # path('stuapi/<int:pk>',Studentretrive.as_view()),
    # path('stuapi/<int:pk>',Studentupdate.as_view()),
    # path('stuapi/<int:pk>',Studentdelete.as_view()),
    # path('stuapi/',Studentview1.as_view()),
    # path('stuapi/<int:pk>',Studentview2.as_view())
    path('stulistapiview/<int:pk>',Studentlistapiview.as_view()),


]
