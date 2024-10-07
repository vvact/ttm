from rest_framework import serializers
from .models import Article
from apps.categories.serializers import CategorySerializer

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    category = CategorySerializer()
    slug = serializers.ReadOnlyField()  # Make slug read-only

    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'content', 'author', 'category', 'created_at', 'updated_at', 'status']
