from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('studentviewset',Student_viewset,basename='student')



urlpatterns = [
    path('fapi/',get_student_api),
    path('fapi/<int:id>/',get_student_api),
    path('fapi/',Student_api.as_view()),
    path('fapi/<int:id>/',Student_api.as_view()),
    path('fapi/',Genric_student_view.as_view()),
    path('fapi/<int:pk>/',Generic_student_api_view2.as_view()),
    path('fapi/',Concrete_view1.as_view()),
    path('fapi/<int:pk>/',Concrete_view2.as_view()),
    path('fapi/',include(router.urls)),

]
