from django.urls import path
from .views import *


urlpatterns = [
    path('setcookie/',setMycookie),
    path('getcookie/',getMycookie),
    path('visit/',get_visit),
    path('setsession/',setsession),
    path('getsession/',getsession),

]
