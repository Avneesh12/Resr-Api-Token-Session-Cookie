from django.urls import path
from .views import *

urlpatterns = [
    path('',firstapi),
    path('stu/',getstudent),
]
