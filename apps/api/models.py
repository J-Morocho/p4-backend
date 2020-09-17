from django.db import models
from django.utils import timezone
from apps.authentication.models import User


# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Plant(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='plants', on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # No image_url in default plant instance
    image_url = models.URLField(blank=True, null=True)
    is_watered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # frequency = 2 (twice a day)
    frequency = models.IntegerField(default=False)
    # curr time we watered
    watered_at = models.DateTimeField(null=True, blank=True)
    # Increment water count when watered_at is updated
    # if watered_count exceeds frequency then alert user
    watered_count = models.IntegerField(default=False)

    def __str__(self):
        return self.name
