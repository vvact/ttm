from rest_framework import serializers
from .models import Article, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name',]

class ArticleSerializer(serializers.ModelSerializer):
    related_articles = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'content', 'author', 'category', 'published_at', 
                  'thumbnail','related_articles']

    def get_related_articles(self, obj):
        # Fetch articles from the same category, excluding the current article
        related = Article.objects.filter(category=obj.category).exclude(id=obj.id).order_by('-published_at')[:5]
        return ArticleSerializer(related, many=True).data
