from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.exceptions import (ValidationError, PermissionDenied)
from rest_framework.permissions import IsAuthenticated
from apps.api.serializers import CategorySerializer, PlantSerializer
from apps.api.models import Category, Plant

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):

    # Must login to create categories
    permission_classes = (IsAuthenticated,)

    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all().filter(
            owner=self.request.user
        )
        return queryset

    def create(self, request, *args, **kwargs):
        # Check if the category already exists for the logged in user
        category = Category.objects.filter(
            name=request.data.get('name'),
            owner=request.user
        )

        if category:
            msg = 'Category with that name already exists',
            raise ValidationError(msg)
        return super().create(request)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SingleCategoryPlant(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlantSerializer

    def get_queryset(self):
        if self.kwargs.get('category_pk') and self.kwargs.get('pk'):
            category = Category.objects.get(pk=self.kwargs['category_pk'])
            queryset = Plant.objects.filter(
                pk=self.kwargs['pk'],
                owner=self.request.user,
                category=category
            )
        return queryset


# Get all plants in a category
class CategoryPlants(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlantSerializer

    def get_queryset(self):
        if self.kwargs.get("category_pk"):
            category = Category.objects.get(pk=self.kwargs['category_pk'])
            queryset = Plant.objects.filter(
                owner=self.request.user,
                category=category
            )
        return queryset


# Get all plants for a logged in user
# Create a plant
class PlantViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlantSerializer

    def get_queryset(self):
        queryset = Plant.objects.all().filter(owner=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied(
                "Only logged in users can create a new plant object"
            )
        print(request)
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        plant = Plant.objects.get(pk=self.kwargs['pk'])
        # Check if the user owns the plant object
        if not request.user == plant.owner:
            raise PermissionDenied(
                "You have no permissions to delete this object"
            )
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def update(self, request, *args, **kwargs):
        plant = Plant.objects.get(pk=self.kwargs['pk'])
        if not request.user == plant.owner:
            raise PermissionDenied(
                'You have no permission to edit this plant object'
            )
        return super().update(request, *args, **kwargs)
