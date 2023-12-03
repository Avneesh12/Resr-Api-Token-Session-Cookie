from django.urls import path
from .views import *


urlpatterns = [
    path('stu/',student_view),
    path('perdel/',personal_view),
    path('paydel/',payment_view),
    path('coursedel/',course_view),
    path('getdel/',get_student),
    path('myform/',myform),
    path('stuimg/',Student_img_view),

] 
