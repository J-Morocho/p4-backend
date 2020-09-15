from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from apps.api.views import CategoryViewSet, PlantViewSet, CategoryPlants

router = routers.DefaultRouter()

router.register('categories', CategoryViewSet, basename='categories')
router.register('plants', PlantViewSet, basename='plants')

custom_urlpatterns = [
    url(r'categories/(?P<category_pk>\d+)/plants$', CategoryPlants.as_view(), name='category_plants'),

]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns
