from django.urls import path
from .views import *

urlpatterns = [
    path('stu/',Classview.as_view()),
    path('stu/<int:id>',Classview.as_view()),
    path('mstu/',Mixinview.as_view()),
    path('mstu/<int:pk>',Mixinview2.as_view()),
    path('cstu/',Concreteapiview.as_view()),
    path('cstu/<int:pk>',Concreteapiview.as_view()),


]
