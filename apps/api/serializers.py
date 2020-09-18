from rest_framework import serializers
from apps.api.models import Category, Plant


class PlantSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Plant
        fields = ('id', 'category', 'owner', 'name', 'description',
                  'image_url', 'is_watered', 'frequency', 'watered_at', 'watered_count', 'created_at', 'updated_at')


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # TODO: What is required=False argument doing?
    plants = PlantSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Category
        fields = ('id', 'name', 'owner', 'plants', 'created_at', 'updated_at')
