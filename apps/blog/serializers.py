from rest_framework import serializers
from .models import Article, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name',]

class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'content', 'author', 'category', 'published_at', 'thumbnail']
