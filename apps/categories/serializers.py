from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()  # Ensure the slug is read-only

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
