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