from rest_framework import viewsets
from .models import Article, Category
from .serializers import ArticleSerializer, CategorySerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'  # Use slug instead of ID for retrieving articles

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'  # Use primary key (ID) for categories
