from django.urls import path
from .views import *

urlpatterns = [
    path('empview/',emp_view),
    path('empadd/',emp_add),
    path('test/',test_api),
]
