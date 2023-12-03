
from django.db import router
from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stuvset/',Studentapi,basename='Student')

router.register('modelvset/',Studentmodelviewset,basename='Student Model Viewset')

router.register('readonlyvset/',StudentReadOnlyvset,basename='Read only Viewset')

urlpatterns = [
    path('',include(router.urls)),
    # path('mvset/',include(router.urls)),
]
