from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('ctoken/',user_token),
    path('secure/',secure_view),
    path('obtoken/',obtain_auth_token),
    # path('getdel/',Get_Details.as_view()),
]
