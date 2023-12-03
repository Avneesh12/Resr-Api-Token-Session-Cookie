from django.urls import path
from .views import *

urlpatterns = [
    # path('fun1/',api_get),
    # path('fun1/<int:id>/',api_get),
    # path('fun2/',api_post),
    path('myapiview/',Studentview.as_view()),
    path('myapiview/<int:id>',Studentview.as_view()),

]
