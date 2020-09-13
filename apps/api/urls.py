from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from apps.api.views import CategoryViewSet, PlantViewSet

router = routers.DefaultRouter()

router.register('categories', CategoryViewSet, basename='categories')
router.register('plants', PlantViewSet, basename='plants')

urlpatterns = [
    path('', include(router.urls)),
]