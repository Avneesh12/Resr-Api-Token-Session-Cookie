from django.urls import path
from .views import *

urlpatterns = [
    path('stu/',student),
    path('stu/<int:id>/',student),
    path('cstu/',Studentapi.as_view()),
    path('cstu/<int:id>',Studentapi.as_view()),
    path('gstu/',Studentgenricview.as_view()),
    path('gstu/<int:pk>/',Studentgenricview2.as_view()),
    path('constu/',Studentconcretwview.as_view()),
    path('constu/<int:pk>/',Studentconcretwview2.as_view()),


]
