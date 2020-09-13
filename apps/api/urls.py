from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from apps.api.views import CategoryViewSet

router = routers.DefaultRouter()

router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('', include(router.urls)),
]